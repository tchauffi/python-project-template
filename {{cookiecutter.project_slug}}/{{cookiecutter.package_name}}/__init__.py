"""{{ cookiecutter.project_description }}"""

__version__ = "{{ cookiecutter.version }}"
__author__ = "{{ cookiecutter.author_name }}"
__email__ = "{{ cookiecutter.author_email }}"

import warnings
try:
    from .main import main
except ImportError as e:
    main = None
    warnings.warn(f"Could not import 'main' from '.main': {e}", ImportWarning)

__all__ = ["main"]
