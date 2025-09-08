## Installing (as editable) using UV tool

```bash
(pyscaffold) ➜  uv tool install --editable .
Resolved 9 packages in 134ms
   Built pyscaffold @ file:///home/papunmohanty/WorkSpace/PythonSpace/PyScaffold/pyscaffold
Prepared 1 package in 855ms
Installed 9 packages in 25ms
 + click==8.2.1
 + markdown-it-py==4.0.0
 + mdurl==0.1.2
 + pygments==2.19.2
 + pyscaffold==0.1.0 (from file:///home/papunmohanty/WorkSpace/PythonSpace/PyScaffold/pyscaffold)
 + rich==14.1.0
 + shellingham==1.5.4
 + typer==0.16.1
 + typing-extensions==4.14.1
warning: The package `typer==0.16.1` does not have an extra named `all`
Installed 1 executable: pyscaffold
```

# Usage:

## Default project creation

```bash
➜ scaffold project generate
Project created...
➜ tree .
.
├── app
│   ├── commands
│   │   ├── base.py
│   │   ├── command1.py
│   │   ├── command2.py
│   │   └── __init__.py
│   ├── core
│   │   ├── config.py
│   │   ├── __init__.py
│   │   ├── logging.py
│   │   └── utils.py
│   ├── __init__.py
│   ├── main.py
│   └── settings.py
├── Makefile
├── pyproject.toml
├── README.md
├── requirements.txt
├── setup.py
└── tests
    ├── __init__.py
    ├── test_command1.py
    ├── test_command2.py
    └── test_config.py

4 directories, 20 files
```

## Default project creation using `uvx` command

```bash
uvx --from pscaffold scaffold project generate
```

## Installation from a file location containing project structure

```bash
➜ scaffold project generate --structure-path sample_struct.json
Project created...
➜ tree .
.
├── app
│   ├── commands
│   │   ├── base.py
│   │   ├── command1.py
│   │   ├── command2.py
│   │   └── __init__.py
│   ├── core
│   │   ├── config.py
│   │   ├── __init__.py
│   │   ├── logging.py
│   │   └── utils.py
│   ├── __init__.py
│   ├── main.py
│   └── settings.py
├── Makefile
├── pyproject.toml
├── README.md
├── requirements.txt
├── sample_struct.json
├── setup.py
├── tests
│   ├── __init__.py
│   ├── test_command1.py
│   ├── test_command2.py
│   └── test_config.py
└── tree_to_json.py

4 directories, 22 files
```
