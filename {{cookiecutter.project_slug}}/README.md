# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Installation

This project uses [Poetry](https://python-poetry.org/) for dependency management.

1. Install Poetry if you haven't already:

   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. Install dependencies:

   ```bash
   poetry install
   ```

3. Activate the virtual environment:

   ```bash
   poetry shell
   ```

## Development

### Code Quality

This project uses [Ruff](https://docs.astral.sh/ruff/) for linting and formatting.

- Format code: `poetry run ruff format`
- Lint code: `poetry run ruff check`
- Fix linting issues: `poetry run ruff check --fix`

### Testing

Run tests with:

```bash
poetry run pytest
```

{% if cookiecutter.use_pre_commit == "y" -%}

### Pre-commit Hooks

This project uses pre-commit hooks to ensure code quality.

1. Install pre-commit hooks:

   ```bash
   poetry run pre-commit install
   ```

2. Run pre-commit on all files:

   ```bash
   poetry run pre-commit run --all-files
   ```

{% endif -%}

## Usage

```python
from {{ cookiecutter.package_name }} import main

main()
```

## License

{% if cookiecutter.license != "None" -%}
This project is licensed under the {{ cookiecutter.license }} License - see the [LICENSE](LICENSE) file for details.
{% else -%}
This project is not licensed.
{% endif -%}
