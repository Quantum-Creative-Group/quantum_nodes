"""Script to run the test suite for a given os and blender version."""
import os
import sys
import zipfile
from pathlib import Path

from scripts.utils import PackageAndAddonUtils as PAU
from scripts.utils import TerminalDisplay as TERM
from scripts.utils import FilesUtils
from scripts.utils import parser

print(f"{TERM.LIGHT_BLUE}{TERM.centered_str(' TEST SUITE: START ', '=')}{TERM.RESET}")

# Check that blender-addon-tester is installed
try:
    import blender_addon_tester as BAT
except Exception as e:
    print(e)
    sys.exit(1)

if __name__ == "__main__":

    args = parser.parse_args()

    if args.b is None:
        print(f"{TERM.LIGHT_RED}ERROR: -b option is None.{TERM.RESET}")
        parser.parse_args(['-h'])

    blender = args.b

    if args.os is None:
        print(f"{TERM.LIGHT_RED}ERROR: -os option is None.{TERM.RESET}")
        parser.parse_args(['-h'])

    system = args.os

    if not ['macos-latest', 'ubuntu-latest', 'windows-latest'] in system:
        print(f"{TERM.LIGHT_RED}ERROR: -os option must be one of\
            ['macos-latest', 'ubuntu-latest', 'windows-latest'].{TERM.RESET}")
        parser.parse_args(['-h'])

    module = "quantum_nodes"
    here = Path(__file__).parent
    addon = os.path.join(os.path.abspath('.'), module)
    cache = os.path.abspath(here.joinpath("../cache").as_posix())
    python = PAU.get_python_version(blender)

    try:
        # Cleanup '__pychache__' folders in the module folder
        FilesUtils.remove_folders_matching_pattern(addon)

        # Download addons on which this add-on depends
        PAU.ANIMATION_NODES["path"] = PAU.download_blender_addon(f"{PAU.ANIMATION_NODES[system]}_py{python}.zip",
                                                                 PAU.ANIMATION_NODES['module'], cache)
        os.environ[f"{PAU.ANIMATION_NODES['module']}_module"] = PAU.ANIMATION_NODES['module']
        os.environ[f"{PAU.ANIMATION_NODES['module']}_path"] = PAU.ANIMATION_NODES['path']

        # Zip addon
        print(f"Zipping addon - path: {PAU.ANIMATION_NODES['path']}")
        zipf = zipfile.ZipFile(module + ".zip", 'w', zipfile.ZIP_DEFLATED)
        FilesUtils.zipdir("./" + module, zipf)
        zipf.close()
        addon = os.path.join(os.path.abspath("."), module + ".zip")

    except Exception as e:
        print(e)
        exit_val = 1
