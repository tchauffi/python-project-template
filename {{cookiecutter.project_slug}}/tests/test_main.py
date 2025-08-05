"""Tests for {{ cookiecutter.package_name }}."""

import pytest

from {{ cookiecutter.package_name }} import __version__


def test_version():
    """Test that version is accessible."""
    assert __version__ == "{{ cookiecutter.version }}"


def test_main(capsys):
    """Test main function."""
    from {{ cookiecutter.package_name }}.main import main
    
    main()
    captured = capsys.readouterr()
    assert "Hello from {{ cookiecutter.project_name }}!" in captured.out
