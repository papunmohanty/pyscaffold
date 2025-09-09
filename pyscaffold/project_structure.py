import os
import typer
import pathlib
from rich import print

from .services.generate_structure import entrypoint


project_app = typer.Typer()


@project_app.command()
def generate(project_name: str = "", project_path: str = "", format: str = "", structure_path: str = "", online_path: str = ""):
    if structure_path and online_path:
        raise typer.BadParameter("Cannot provide both --structure-path and --online-path. Please choose one.")
    try:
        if project_path in ('', "\n"):
            project_path = f"{os.getcwd()}/{project_name}"
        elif project_name not in ('', "\n"):
            project_path = f"{os.getcwd()}/{project_path}/{project_name}"
        root_path = pathlib.Path(project_path).absolute()
        if structure_path:
            path_type = "file"
            entrypoint(root_path, structure_path, path_type)
        elif online_path:
            path_type = "online_json"
            entrypoint(root_path, online_path, path_type)
        else:
            raise ValueError("Path Type for Json Structure Location Not Defined")
        print("Project created...")
    except Exception as err:
        print(f"Error generating project structure: {err}")
