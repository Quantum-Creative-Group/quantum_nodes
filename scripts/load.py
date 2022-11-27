"""Run the test suite inside blender."""

import os
import sys
from pathlib import Path

# Make utils.py functions available in this file
sys.path.append(os.path.abspath("."))

from scripts.utils import TerminalDisplay as TERM
from scripts.utils import PackageAndAddonUtils as PAU
from scripts.utils import FilesUtils

print(f"{TERM.LIGHT_BLUE}{TERM.centered_str(' LOAD PYTEST ', '=')}{TERM.RESET}")
print("Running file:", __file__, "from Blender.")

# +---------------------------------------------------------+
# + GET TEST SUITE CONFIGURATION FROM ENVIRONMENT VARIABLES +
# +---------------------------------------------------------+

# Make sure to have BLENDER_ADDON_TO_TEST set as an environment variable first
ADDON = os.environ.get("BLENDER_ADDON_TO_TEST", False)
if not ADDON:
    print("ERROR: no add-on to test was found in the 'BLENDER_ADDON_TO_TEST' environment variable.")
    sys.exit(1)

# Set any value to the BLENDER_ADDON_COVERAGE_REPORTING environment variable to enable it
COVERAGE_REPORTING = os.environ.get("BLENDER_ADDON_COVERAGE_REPORTING", False)

# The Pytest tests/ path can be overridden through the BLENDER_ADDON_TESTS_PATH environment variable
default_tests_dir = Path(ADDON).parent.joinpath("tests")
TESTS_PATH = os.environ.get("BLENDER_ADDON_TESTS_PATH", default_tests_dir.as_posix())

# +----------------------+
# + INSTALL REQUIREMENTS +
# +----------------------+

try:
    import PIL
    import scipy
    import numpy
    import qiskit
    import qiskit_finance
    import qiskit_machine_learning

    import pytest
    import blender_addon_tester

except Exception as e:
    print(f"{TERM.LIGHT_YELLOW}Missing module...{TERM.RESET}", e)
    print(f"{TERM.LIGHT_YELLOW}Trying to install missing dependencies...{TERM.RESET}")
    try:
        PAU.install_py_requirements(os.path.join(os.path.abspath("."), "requirements.txt"), force=True)
    except Exception as e:
        print(e)
        sys.exit(1)

# Import unit testing utils functions
import blender_addon_tester.addon_helper as BAT


class SetupPlugin:
    """Setup class for pytest."""

    def __init__(self, addon: str, addon_dir: str = os.path.abspath("./local_addon/")):
        """
        Init method of the class.

        Args:
            addon (sstr): absolute path to the addon (zip file)
        """

        self.root = Path(__file__).parent.parent
        self.addon = addon
        self.addon_dir = addon_dir
        self.bpy_module = None
        self.zfile = None

    def pytest_configure(self, config: dict):
        """
        Configure pytest.

        Args:
            config (dict): configuration
        """

        print("PyTest configure...")

        self.bpy_module, self.zfile = BAT.zip_addon(self.addon, self.addon_dir)
        BAT.change_addon_dir(self.bpy_module, self.addon_dir)
        BAT.install_addon(
            os.environ.get(f"{PAU.ANIMATION_NODES['module']}_module", None),
            os.environ.get(f"{PAU.ANIMATION_NODES['module']}_path", None)
        )
        BAT.install_addon(self.bpy_module, self.zfile)
        config.cache.set("bpy_module", self.bpy_module)

        print("PyTest configure successful!")

    def pytest_unconfigure(self):
        """Unconfigure pytest."""

        print("PyTest unconfigure...")

        # Cleanup zip files
        print("Cleaning up - zip files")
        exclude = [os.path.abspath("./cache")]
        FilesUtils.remove_files_matching_pattern(self.root, exclude_folders=exclude, pattern="*.zip")

        BAT.cleanup(None, self.bpy_module, os.path.join(self.addon_dir, "addons", self.bpy_module))

        # TODO: find a better fix to "[WinError 5] Access denied:
        # '[....]\\local_addon\\addons\\animation_nodes\\algorithms\\hashing\\murmurhash3.cp39-win_amd64.pyd'"
        try:
            an_path = os.environ.get(f"{PAU.ANIMATION_NODES['module']}_module", None)
            BAT.cleanup(None, an_path, os.path.join(self.addon_dir, "addons", an_path))
        except BaseException as exception:
            print(f"{TERM.LIGHT_YELLOW}WARNING: failed to clean animation_nodes directory ({an_path}).{TERM.RESET}")

        print("PyTest unconfigure successful!")


try:
    import pytest

    pytest_main_args = ["-x", TESTS_PATH]
    if COVERAGE_REPORTING is not False:
        pytest_main_args += ["--cov", "--cov-report", "term", "--cov-report", "xml"]
    exit_val = pytest.main(pytest_main_args, plugins=[SetupPlugin(ADDON)])

except Exception as e:
    print(e)
    exit_val = 1

sys.exit(exit_val)
