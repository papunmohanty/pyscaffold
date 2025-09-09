import json
import pathlib
import requests
from pyscaffold.config import BASE_CONFIG_PATH
from pyscaffold.constants import PathType


def entrypoint(root_path: pathlib.Path, json_path: str, path_type: str):
    if path_type == PathType.FILE:
        if json_path in ('', "\n"):
            json_path = f"{BASE_CONFIG_PATH}/assets/default.json"
            with open(json_path) as fo:
                project_structure = json.load(fo)
        else:
            with open(json_path) as fo:
                project_structure = json.load(fo)
    elif path_type == PathType.ONLINE_JSON:
        response = requests.get(json_path)
        project_structure = response.json()
    generate_folder_structure(root_path, list(project_structure.values())[0])


def generate_folder_structure(root_path: pathlib.Path, project_structure: list):
    """
    Generates a folder structure from a given list of file and directory names.

    It's a recursive function that iterates over the project_structure list. If an element is a string,
    it treats it as a filepath and creates it. If an element is a dictionary, it treats it as a directory
    and creates it, then recursively calls itself with the new directory as the root path
    and the dictionary's values as the project structure.

    Args:
    root_path (pathlib.Path): The base directory where the folder structure should be created.
                            Existing directories in the path will not be removed or modified, but new
                            directories and files will be created as needed.
    
    project_structure (List): A list containing the names of files and directories to be created.
                            Each element in the list can be either a string or a dictionary.
                            - If it's a string, a file with that name will be created in the
                                current root path.
                            - If it's a dictionary, a directory will be created with
                                the name being the key of the dictionary. The value of the dictionary
                                should be another list following the same rules, representing the contents
                                of the new directory.

    Returns:
    No return value. The function works by causing side effects (i.e., creating files and directories).
    """
    root_path.mkdir(parents=True, exist_ok=True)
    for element in project_structure:
        if isinstance(element, str):
            filepath = root_path / element
            filepath.touch()
        else: # Else, it is a dictionary
            folder_name = list(element.keys())[0]
            folder_path = root_path / folder_name
            pathlib.Path(folder_path).mkdir(parents=True, exist_ok=True)
            generate_folder_structure(
                folder_path,
                list(element.values())[0]
            )
