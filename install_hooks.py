"""This is the main module of the application."""

import os
from pathlib import Path
import stat


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
    hooks_dir = "hooks"
    git_hooks_dir = ".git/hooks"

    # Iterate over each subdirectory in the hooks directory
    for stage_dir in os.listdir(hooks_dir):
        stage_path = os.path.join(hooks_dir, stage_dir)

        if os.path.isdir(stage_path):
            hook_file_path = os.path.join(git_hooks_dir, stage_dir)

            # Create or overwrite the hook script
            with open(hook_file_path, "w", encoding="utf-8") as hook_file:
                hook_file.write("#!/bin/bash\n\n")
                hook_file.write(f"# Run scripts for the {stage_dir} hook\n\n")

                # Iterate over each script in the current stage directory
                for script in os.listdir(stage_path):
                    script_path = os.path.join(stage_path, script)

                    if os.path.isfile(script_path) and os.access(script_path, os.X_OK):
                        hook_file.write(f"echo Running {Path(script_path).name}...\n")
                        hook_file.write(
                            f'"{script_path}" || {{ echo "Error: {script_path} failed."; exit 1; }}\n'
                        )
                    else:
                        hook_file.write(
                            f"echo Skipping {script_path} (not executable).\n"
                        )

            make_executable(Path(hook_file_path))
            print(f"Installed {stage_dir} hook successfully.")

    print("All hooks installed successfully.")


if __name__ == "__main__":
    main()
