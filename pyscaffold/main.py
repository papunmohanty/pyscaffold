import typer
from rich import print
from pyscaffold.project_structure import project_app

app = typer.Typer()


app.add_typer(project_app, name="project")
