"""This is the main module of the application."""

from enum import Enum
import os
from pathlib import Path
import shutil
import stat


class Color(Enum):
    """Define colors for the terminal output."""

    RESET = "\033[0m"
    YELLOW = "\033[0;33m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"


def make_executable(file_path: Path) -> None:
    """
    Make the file executable by the owner, group, and others.

    Args:
        file_path (Path): The path to the file that should be made executable.
    """
    current_permissions = os.stat(file_path).st_mode
    new_permissions = current_permissions | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH
    os.chmod(file_path, new_permissions)


def main() -> None:
    """Install the hooks in the .git/hooks directory."""
    # Define the source and destination directories
    source_file = "hooks/run_hooks.sh"
    destination_dir = ".git/hooks"

    # List of git stages
    git_stages = (
        "applypatch-msg",
        "commit-msg",
        "fsmonitor-watchman",
        "post-update",
        "pre-applypatch",
        "pre-commit",
        "pre-merge-commit",
        "pre-push",
        "pre-rebase",
        "pre-receive",
        "prepare-commit-msg",
        "update",
    )

    # Ensure the destination directory exists
    os.makedirs(destination_dir, exist_ok=True)

    # Copy the hook script to each git stage
    for stage in git_stages:
        destination_file = os.path.join(destination_dir, stage)
        shutil.copyfile(source_file, destination_file)
        make_executable(Path(destination_file))

    print(
        f"{Color.GREEN.value}Successfully installed hooks in the .git/hooks directory.{Color.RESET.value}"
    )


if __name__ == "__main__":
    main()
