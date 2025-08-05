#!/usr/bin/env python3
"""Post-generation hook for the Python project template."""

import os
import subprocess
import sys


def remove_file_if_exists(filepath):
    """Remove a file if it exists."""
    if os.path.exists(filepath):
        os.remove(filepath)
        print(f"Removed {filepath}")


def remove_dir_if_exists(dirpath):
    """Remove a directory if it exists."""
    if os.path.exists(dirpath):
        import shutil
        shutil.rmtree(dirpath)
        print(f"Removed {dirpath}")


def main():
    """Main post-generation hook."""
    
    # Remove files based on user choices
    if "{{ cookiecutter.use_github_actions }}" == "n":
        remove_dir_if_exists(".github")
    
    if "{{ cookiecutter.use_pre_commit }}" == "n":
        remove_file_if_exists(".pre-commit-config.yaml")
    
    if "{{ cookiecutter.use_docker }}" == "n":
        remove_file_if_exists("Dockerfile")
    
    if "{{ cookiecutter.include_notebooks }}" == "n":
        remove_dir_if_exists("notebooks")
    
    if "{{ cookiecutter.license }}" == "None":
        remove_file_if_exists("LICENSE")
    
    # Initialize git repository
    try:
        subprocess.run(["git", "init"], check=True, capture_output=True)
        print("Initialized git repository")
        
        subprocess.run(["git", "add", "."], check=True, capture_output=True)
        subprocess.run(["git", "commit", "-m", "Initial commit"], check=True, capture_output=True)
        print("Created initial commit")
        
    except subprocess.CalledProcessError as e:
        print(f"Warning: Could not initialize git repository: {e}")
    
    # Print success message and next steps
    print("\n" + "="*60)
    print(f"🎉 Successfully created {{ cookiecutter.project_name }}!")
    print("="*60)
    print("\nNext steps:")
    print("1. cd {{ cookiecutter.project_slug }}")
    print("2. Install Poetry: curl -sSL https://install.python-poetry.org | python3 -")
    print("3. Install dependencies: poetry install")
    
    if "{{ cookiecutter.use_pre_commit }}" == "y":
        print("4. Set up pre-commit: poetry run pre-commit install")
    
    print("\nHappy coding! 🚀")


if __name__ == "__main__":
    main()
