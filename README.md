# Python Project Template

A modern Python project template using [Cookiecutter](https://cookiecutter.readthedocs.io/) with best practices and modern tooling.

## Features

This template provides:

- **🐍 Python 3.10+** support with configurable Python versions
- **📦 Poetry** for dependency management and packaging
- **🧹 Ruff** for fast linting and code formatting
- **🧪 pytest** for testing framework
- **🔄 Pre-commit hooks** for code quality enforcement
- **🚀 GitHub Actions** CI/CD workflows
- **🐳 Docker** support (optional)
- **📄 Multiple license options** (MIT, Apache-2.0, GPL-3.0, BSD-3-Clause, or None)
- **📚 Comprehensive documentation** and development setup guides
- **🛠️ Makefile** with common development tasks
- **📁 Well-structured project layout**

## Quick Start

### Prerequisites

- [Python 3.10+](https://www.python.org/downloads/)
- [Cookiecutter](https://cookiecutter.readthedocs.io/en/stable/installation.html)

Install Cookiecutter:

```bash
pip install cookiecutter
```

### Generate a New Project

```bash
cookiecutter https://github.com/tchauffi/python-project-template
```

Or use it locally:

```bash
cookiecutter /path/to/python-project-template
```

### Using as GitHub Template

This repository is configured as a GitHub template. You can also:

1. Click the **"Use this template"** button on GitHub
2. Create a new repository from this template
3. Clone your new repository
4. Run cookiecutter to generate the project structure:
   ```bash
   cookiecutter .
   ```

### Template Options

When you run the template, you'll be prompted for the following options:

| Option | Description | Default | Choices |
|--------|-------------|---------|---------|
| `project_name` | The name of your project | "My Python Project" | Any string |
| `project_slug` | URL/directory friendly name | Auto-generated from project_name | Auto-generated |
| `package_name` | Python package name | Auto-generated from project_slug | Auto-generated |
| `project_description` | Brief project description | "A brief description of the project" | Any string |
| `author_name` | Your name | "Your Name" | Any string |
| `author_email` | Your email | "your.email@example.com" | Any email |
| `github_username` | Your GitHub username | "yourusername" | Any string |
| `version` | Initial version | "0.1.0" | Any version string |
| `python_version` | Supported Python versions | ["3.10", "3.11", "3.12"] | List of versions |
| `min_python_version` | Minimum Python version | "3.10" | Any version |
| `use_github_actions` | Include GitHub Actions CI | "y" | y/n |
| `use_pre_commit` | Include pre-commit hooks | "y" | y/n |
| `license` | Project license | "MIT" | MIT/Apache-2.0/GPL-3.0/BSD-3-Clause/None |
| `use_docker` | Include Docker configuration | "y" | y/n |

## Generated Project Structure

```
your-project/
├── your_package/           # Main Python package
│   ├── __init__.py
│   └── main.py            # Main module (if example code enabled)
├── tests/                 # Test directory
│   ├── __init__.py
│   └── test_main.py       # Example tests
├── .github/               # GitHub Actions workflows
│   └── workflows/
│       └── ci.yml
├── pyproject.toml         # Poetry configuration and tool settings
├── README.md              # Project documentation
├── DEVELOPMENT.md         # Development setup guide
├── Makefile              # Development commands
├── .gitignore            # Git ignore rules
├── .pre-commit-config.yaml # Pre-commit configuration
├── Dockerfile            # Docker configuration (optional)
└── LICENSE               # License file (if license selected)
```

## Development Workflow

After generating your project:

1. **Navigate to your project:**
   ```bash
   cd your-project-name
   ```

2. **Install Poetry** (if not already installed):
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

3. **Install dependencies:**
   ```bash
   poetry install
   ```

4. **Set up pre-commit hooks** (if enabled):
   ```bash
   poetry run pre-commit install
   ```

5. **Start developing!**
   ```bash
   poetry shell  # Activate virtual environment
   make help     # See available commands
   ```

## Available Make Commands

The generated project includes a Makefile with common development tasks:

- `make help` - Show all available commands
- `make install` - Install project dependencies
- `make dev-install` - Install development dependencies
- `make test` - Run tests
- `make test-cov` - Run tests with coverage
- `make lint` - Run Ruff linter
- `make format` - Format code with Ruff
- `make fix` - Fix automatically fixable linting issues
- `make clean` - Clean build artifacts
- `make build` - Build the package
- `make run` - Run the application

## Tool Configuration

### Ruff

The template includes a comprehensive Ruff configuration in `pyproject.toml`:

- **Line length:** 88 characters
- **Target Python version:** Configurable (default: 3.10+)
- **Enabled rules:** pycodestyle, pyflakes, isort, flake8-bugbear, flake8-comprehensions, pyupgrade
- **Format style:** Double quotes, space indentation

### pytest

Basic pytest configuration for running tests:

- **Test directory:** `tests/`
- **Test file pattern:** `test_*.py`
- **Test function pattern:** `test_*`

### Pre-commit

Includes hooks for:

- Trailing whitespace removal
- End-of-file fixer
- YAML/TOML validation
- Large file detection
- Merge conflict detection
- Ruff linting and formatting
- Poetry validation

### GitHub Actions

The CI workflow includes:

- **Multi-Python version testing** (3.10, 3.11, 3.12)
- **Dependency caching** for faster builds
- **Code quality checks** with Ruff
- **Test execution** with pytest
- **Poetry** for dependency management

## Customization

You can customize the template by:

1. **Forking this repository**
2. **Modifying the template files** in `{{cookiecutter.project_slug}}/`
3. **Updating the configuration** in `cookiecutter.json`
4. **Adjusting the post-generation hook** in `hooks/post_gen_project.py`

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Testing the Template

To test the template locally:

```bash
# Test with default values
cookiecutter . --no-input

# Test with custom values
cookiecutter . --no-input --extra-context '{"project_name": "Test Project", "use_github_actions": "n"}'

# Validate generated YAML files
python -c "import yaml; yaml.safe_load(open('test-project/.github/workflows/ci.yml'))"
```

## GitHub Template Setup

To use this as a GitHub template repository:

1. **Enable Template Repository**:
   - Go to **Settings** → **General**
   - Check **"Template repository"**
   - Save changes

2. **Users can then**:
   - Click **"Use this template"** on GitHub
   - Create a new repository
   - Clone and run: `cookiecutter .`

## License

This template is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Cookiecutter](https://cookiecutter.readthedocs.io/) for the templating system
- [Poetry](https://python-poetry.org/) for modern Python packaging
- [Ruff](https://docs.astral.sh/ruff/) for fast Python linting and formatting
- [pytest](https://pytest.org/) for testing framework
- [pre-commit](https://pre-commit.com/) for code quality hooks
