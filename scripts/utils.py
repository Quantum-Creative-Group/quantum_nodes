"""Utility functions and classes to setup the unit testing environment."""

import os
import sys
import shutil
import fnmatch
import zipfile
import requests
import argparse
import subprocess

# Parser for test.py
parser = argparse.ArgumentParser(description="Add-on test suite")
parser.add_argument(
    "-b",
    metavar="Blender version",
    type=str,
    nargs='?',
    default="3.0.0",
    help="Version of Blender to test."
)
parser.add_argument(
    "-os",
    metavar="Operating system",
    type=str,
    nargs='?',
    default="ubuntu",
    help="Operating system on which to run tests: ['macos-latest', 'ubuntu-latest', 'windows-latest']."
)


class TerminalDisplay:
    """Useful tools to better the messages displayed in the terminal."""

    # List of colors which can be used to color texts in the terminal.
    LIGHT_RED = '\033[91m'
    LIGHT_GREEN = '\033[92m'
    LIGHT_YELLOW = '\033[93m'
    LIGHT_BLUE = '\033[94m'
    LIGHT_MAGENTA = '\033[95m'
    LIGHT_CYAN = '\033[96m'

    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

    @classmethod
    def centered_str(cls, message: str, char: str = "-") -> str:
        """
        Generate a line full of 'char' with the given message at the center.

        Args:
            message (str): message to display.
            char (str, optional): char with which to fill the line. Defaults to "-".

        Returns:
            str: generated line
        """

        terminal_size = shutil.get_terminal_size((80, 20))
        return message.center(terminal_size.columns, char)


class PackageAndAddonUtils:
    """Utility methods to manage python packages and blender add-ons."""

    ANIMATION_NODES = {
        "module": "animation_nodes",
        "path": "",
        "windows-latest": "https://github.com/JacquesLucke/animation_nodes/releases/download/master-cd-build/animation_nodes_v2_3_windows",     # noqa: E501
        "ubuntu-latest": "https://github.com/JacquesLucke/animation_nodes/releases/download/master-cd-build/animation_nodes_v2_3_linux",        # noqa: E501
        "macos-latest": "https://github.com/JacquesLucke/animation_nodes/releases/download/master-cd-build/animation_nodes_v2_3_macOS",         # noqa: E501
    }

    @classmethod
    def get_python_version(cls, blender: str) -> str:
        """
        Get the python version used by the given blender version.

        Args:
            blender (str): blender version (format: major.minor.patch).

        Returns:
            str: python version used by Blender (MajorMinor).
        """

        if any(version in blender for version in ["2.9", "3.0"]):
            return "39"

        if any(version in blender for version in ["3.1", "3.2", "3.3", "3.4"]):
            return "310"

        raise ValueError(f"Unable to determine which python version is used by the given blender version ({blender})")

    @classmethod
    def install_py_package(cls, package: str, force: bool = False) -> None:
        """
        Install the given python package.

        Args:
            package (str): name of the package.
            force (bool, optional): force reinstall. Defaults to False.
        """

        args = [sys.executable, "-m", "pip", "install", package, "--user"]
        if force:
            args.append("--force-reinstall")
        subprocess.check_call(args)

    @classmethod
    def install_py_requirements(cls, requirements: str, force: bool = False) -> None:
        """
        Install python packages from the given requirements file.

        Args:
            requirements (str): path to the requirements file.
            force (bool, optional): force reinstall. Defaults to False.
        """

        args = [sys.executable, "-m", "pip", "install", "-r", requirements, "--upgrade", "--user"]
        if force:
            args.append("--force-reinstall")
        subprocess.check_call(args)

    @classmethod
    def install_local_py_package(cls, path: str, force: bool = False) -> None:
        """
        Install a local package.

        Args:
            path (str): path to the folder of the local package.
            force (bool, optional): force reinstall. Defaults to False.
        """

        args = [sys.executable, "-m", "pip", "install", "-e", path]
        if force:
            args.append("--force-reinstall")
        subprocess.check_call(args)

    @classmethod
    def download_blender_addon(cls, url: str, name: str, dest: str) -> str:
        """
        Download the given blender add-on and put it in the destination folder.

        Args:
            url (str): base url to download the file.
            name (str): name of the add-on's folder.
            dest (str): destination of the downloaded file.

        Returns:
            str: path to the zip file
        """

        filename = f"{name}.zip"
        path = os.path.abspath(os.path.join(dest, filename))

        if not os.path.exists(dest):
            print(f"The given path does not exist: {dest}")
            os.mkdir(dest)
            print(f"Created destination folder: {dest}")

        if os.path.exists(os.path.join(dest, filename)):
            print(f"{name} - found: {path}")
            return path

        # Else, download it and save it at the given destination
        print(f"Downloading: {filename} ({url})")
        response = requests.get(url)
        open(os.path.join(dest, filename), "wb").write(response.content)

        return path


class FilesUtils:
    """Methods to manage files and folders when setting up the unit testing environment."""

    @classmethod
    def zipdir(cls, path: str, ziph: zipfile.ZipFile) -> None:
        """
        Zip the given folder.

        Args:
            path (str): path to the folder.
            ziph (zipfile.ZipFile): zip file.
        """

        # Inspired from: https://www.tutorialspoint.com/How-to-zip-a-folder-recursively-using-Python
        # ziph is zipfile handle
        for root, dirs, files in os.walk(path):
            for file in files:
                ziph.write(os.path.join(root, file))

    @classmethod
    def remove_files_matching_pattern(cls, root_folder: str, exclude_folders: list[str] = [],
                                      pattern: str = "*.zip") -> None:
        """
        Remove files which name match the given pattern.

        Inspired from:
        https://thispointer.com/python-how-to-remove-files-by-matching-pattern-wildcards-certain-extensions-only/

        Args:
            root_folder (str): root folder.
            exclude_folders (list[str], optional): list of folders to exclude from this function. Defaults to [].
            pattern (str, optional): pattern of the files to remove. Defaults to "*.zip".
        """
        # Get a list of all files in directory
        for rootDir, subdirs, filenames in os.walk(root_folder):
            # Find the files that matches the given pattern
            for filename in fnmatch.filter(filenames, pattern):
                try:
                    if os.path.dirname(os.path.join(rootDir, filename)) not in exclude_folders:
                        os.remove(os.path.join(rootDir, filename))
                except OSError:
                    print("Error while deleting file")

    @classmethod
    def remove_folders_matching_pattern(cls, root_folder: str, pattern: str = "__pycache__") -> None:
        """
        Remove folders which name match the given pattern.

        Args:
            root_folder (str): root folder.
            pattern (str, optional): pattern of the folders to remove. Defaults to "__pycache__".
        """
        # Get a list of all files in directory
        for rootDir, subdirs, filenames in os.walk(root_folder):
            # Find the files that matches the given pattern
            for subdir in subdirs:
                if subdir == pattern:
                    shutil.rmtree(os.path.join(rootDir, subdir), ignore_errors=True)
