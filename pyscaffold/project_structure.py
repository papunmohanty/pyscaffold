import os
import typer
import pathlib
from rich import print

from .services.generate_structure import entrypoint


project_app = typer.Typer()


@project_app.command()
def generate(project_name: str = "", project_path: str = "", format: str = "", structure_path: str = ""):
    try:
        if project_path in ('', "\n"):
            project_path = f"{os.getcwd()}/{project_name}"
        elif project_name not in ('', "\n"):
            project_path = f"{os.getcwd()}/{project_path}/{project_name}"
        root_path = pathlib.Path(project_path).absolute()
        entrypoint(root_path, structure_path)
        print("Project created...")
    except Exception as err:
        print(f"Error generating project structure: {err}")
