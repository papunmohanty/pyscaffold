```bash
➜  pyscaffold git:(master) ✗ uv add "typer[all]"
Using CPython 3.13.0
Creating virtual environment at: .venv
Resolved 10 packages in 32ms
warning: The package `typer==0.16.1` does not have an extra named `all`
warning: The package `typer==0.16.1` does not have an extra named `all`
Installed 8 packages in 37ms
 + click==8.2.1
 + markdown-it-py==4.0.0
 + mdurl==0.1.2
 + pygments==2.19.2
 + rich==14.1.0
 + shellingham==1.5.4
 + typer==0.16.1
 + typing-extensions==4.14.1
```

```bash
➜  pyscaffold git:(master) ✗ uv add --dev "pytest[all]"
Resolved 14 packages in 9ms
warning: The package `pytest==8.4.1` does not have an extra named `all`
warning: The package `typer==0.16.1` does not have an extra named `all`
warning: The package `pytest==8.4.1` does not have an extra named `all`
warning: The package `typer==0.16.1` does not have an extra named `all`
Installed 4 packages in 29ms
 + iniconfig==2.1.0
 + packaging==25.0
 + pluggy==1.6.0
 + pytest==8.4.1
```

```bash
(pyscaffold) ➜  pyscaffold git:(master) ✗ uv tool install --editable .
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
