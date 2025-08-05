# Example Usage

This document shows how to use the Python Project Template to create a new project.

## Installation

First, install Cookiecutter:

```bash
pip install cookiecutter
```

## Generate a Project

### Using defaults (recommended for quick start):

```bash
cookiecutter https://github.com/tchauffi/python-project-template --no-input
```

### Interactive mode (customize all options):

```bash
cookiecutter https://github.com/tchauffi/python-project-template
```

Example interactive session:

```
project_name [My Python Project]: Awesome Data Tool
project_slug [awesome-data-tool]: 
package_name [awesome_data_tool]: 
project_description [A brief description of the project]: A tool for processing and analyzing data
author_name [Your Name]: John Doe
author_email [your.email@example.com]: john.doe@example.com
github_username [yourusername]: johndoe
version [0.1.0]: 
python_version:
  1 - 3.10
  2 - 3.11
  3 - 3.12
Choose from 1, 2, 3 [1]: 2
min_python_version [3.10]: 3.11
use_github_actions [y]: 
use_pre_commit [y]: 
use_ruff [y]: 
use_poetry [y]: 
license:
  1 - MIT
  2 - Apache-2.0
  3 - GPL-3.0
  4 - BSD-3-Clause
  5 - None
Choose from 1, 2, 3, 4, 5 [1]: 1
create_tests [y]: 
use_docker [y]: 
```

## After Generation

Once your project is generated:

1. Navigate to the project directory:
   ```bash
   cd awesome-data-tool
   ```

2. Initialize the development environment:
   ```bash
   make dev-install
   ```

3. Start coding!
   ```bash
   poetry shell
   code .  # Open in VS Code
   ```

## Common Customizations

### Minimal Setup (No CI/Docker)

For a simple local project:

```bash
cookiecutter https://github.com/tchauffi/python-project-template \
  use_github_actions=n \
  use_docker=n \
  use_docker=n
```

### Data Science Project

For a data science project:

```bash
cookiecutter https://github.com/tchauffi/python-project-template \
  project_name="My Data Science Project" \
  use_docker=y
```

Then add data science dependencies to `pyproject.toml`:

```toml
[tool.poetry.dependencies]
python = "^3.11"
pandas = "^2.0.0"
numpy = "^1.24.0"
matplotlib = "^3.7.0"
jupyter = "^1.0.0"
```

### Library Package

For a Python library:

```bash
cookiecutter https://github.com/tchauffi/python-project-template \
  use_docker=n \
  create_tests=y
```
