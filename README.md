<div align="center">
  <h1>🏗️ PyScaffold</h1>
  <p><strong>A powerful Python project scaffolding tool</strong></p>
  <p>Generate well-structured Python projects instantly with customizable templates</p>

  [![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)
  [![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
  [![Version](https://img.shields.io/badge/version-0.1.7-orange.svg)](pyproject.toml)
</div>

---

## ✨ Features

- 🚀 **Lightning Fast**: Generate complete project structures in seconds
- 🎨 **Flexible Templates**: Use built-in templates or create your own JSON configurations
- 🌐 **Remote Support**: Load project structures from online JSON files
- 📁 **Nested Structures**: Create complex directory hierarchies with ease
- 🔧 **CLI Integration**: Beautiful command-line interface powered by Typer
- 🧪 **Well Tested**: Comprehensive test suite ensuring reliability

## 🏃‍♂️ Quick Start

### Installation

Install PyScaffold using UV (recommended):

```bash
# Install as a tool (recommended)
uv tool install pscaffold

# Or install from source (for development)
uv tool install --editable .
```

### Basic Usage

Create a new project with the default template:

```bash
scaffold project generate
```

**Output:**
```
Project created...
```

**Generated Structure:**
```
.
├── app/
│   ├── commands/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── command1.py
│   │   └── command2.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── logging.py
│   │   └── utils.py
│   ├── __init__.py
│   ├── main.py
│   └── settings.py
├── tests/
│   ├── __init__.py
│   ├── test_command1.py
│   ├── test_command2.py
│   └── test_config.py
├── Makefile
├── pyproject.toml
├── README.md
├── requirements.txt
└── setup.py

4 directories, 20 files
```

## 📖 Usage Guide

### 1. Default Project Generation

```bash
# Generate project in current directory
scaffold project generate
```

### 2. Using Custom Templates

Create a custom project structure using a JSON file:

```bash
scaffold project generate --structure-path /path/to/your/my_template.json
```

**Example JSON Template:**
```json
{
    "my_project": [
        {
            "src": [
                "__init__.py",
                "main.py",
                {
                    "utils": [
                        "__init__.py",
                        "helpers.py"
                    ]
                }
            ]
        },
        {
            "tests": [
                "test_main.py"
            ]
        },
        "README.md",
        "requirements.txt"
    ]
}
```

### 3. Remote Templates

Load templates from online sources:

```bash
scaffold project generate --online-path https://raw.githubusercontent.com/user/repo/main/template.json
```

### 4. One-Shot Execution

Run PyScaffold without installing:

```bash
uvx --from pscaffold scaffold project generate
```

## 🛠️ Development

### Setting up for Development

```bash
# Clone the repository
git clone <repository-url>
cd pyscaffold

# Install dependencies
uv sync --dev

# Install in editable mode
uv tool install --editable .
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=pyscaffold
```

### Clean Up

```bash
# Remove cache files
make rmcache

# Remove egg info
make rmeggs
```

## 📁 Project Structure

```
pyscaffold/
├── pyscaffold/
│   ├── assets/
│   │   └── default.json          # Default project template
│   ├── services/
│   │   ├── __init__.py
│   │   └── generate_structure.py # Core generation logic
│   ├── __init__.py
│   ├── config.py                 # Configuration settings
│   ├── constants.py              # Project constants
│   ├── main.py                   # CLI entry point
│   └── project_structure.py      # Project commands
├── tests/
│   ├── __init__.py
│   └── test_generate_folder_structure.py
├── .gitignore
├── .python-version
├── makefile
├── pyproject.toml
├── README.md
└── uv.lock
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Guidelines

- Write tests for new features
- Follow PEP 8 style guidelines
- Update documentation as needed
- Ensure all tests pass

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Links

- **Documentation**: Coming soon!
- **Issues**: [GitHub Issues](https://github.com/papunmohanty/pyscaffold/issues)
- **PyPI Package**: `pscaffold`

## 🙏 Acknowledgments

- Built with [Typer](https://typer.tiangolo.com/) for the CLI interface
- Styled with [Rich](https://rich.readthedocs.io/) for beautiful terminal output
- Powered by [UV](https://docs.astral.sh/uv/) for fast Python package management

---

<div align="center">
  <p>Made with ❤️ by the PyScaffold team</p>
  <p>⭐ Star us on GitHub if this project helped you!</p>
</div>
