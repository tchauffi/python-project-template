# Development Setup

This document describes how to set up the development environment for {{ cookiecutter.project_name }}.

## Prerequisites

- Python {{ cookiecutter.min_python_version }}+
- [Poetry](https://python-poetry.org/) for dependency management

## Initial Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.git
   cd {{ cookiecutter.project_slug }}
   ```

2. Install dependencies:
   ```bash
   make dev-install
   ```

3. Activate the virtual environment:
   ```bash
   poetry shell
   ```

## Development Workflow

### Code Quality

Before committing code, ensure it passes all quality checks:

```bash
# Format code
make format

# Run linter
make lint

# Fix automatically fixable issues
make fix
```

### Testing

Run the test suite:

```bash
# Run tests
make test

# Run tests with coverage
make test-cov
```

{% if cookiecutter.use_pre_commit == "y" -%}
### Pre-commit Hooks

Pre-commit hooks are automatically installed when you run `make dev-install`. They will run on every commit to ensure code quality.

To run pre-commit hooks manually:
```bash
poetry run pre-commit run --all-files
```

{% endif -%}
### Building and Running

```bash
# Build the package
make build

# Run the application
make run
```

## Available Make Commands

Run `make help` to see all available commands.

## Project Structure

```
{{ cookiecutter.project_slug }}/
├── {{ cookiecutter.package_name }}/     # Main package
│   ├── __init__.py
│   └── main.py          # Main module
├── tests/               # Test files
│   ├── __init__.py
│   └── test_main.py
├── .github/             # GitHub Actions workflows
├── pyproject.toml       # Poetry configuration
├── README.md
├── Makefile            # Development commands
{% if cookiecutter.use_pre_commit == "y" -%}
├── .pre-commit-config.yaml
{% endif -%}
└── .gitignore
```
