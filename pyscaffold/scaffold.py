import json
import os
import pathlib


def entrypoint(root_path: pathlib.Path, structure_path: str):
    if structure_path in ('', "\n"):
        structure_path = "example_project_structures/default.json"
    with open(structure_path) as fo:
        project_structure = json.load(fo)
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


if __name__ == "__main__":
    project_name = input("Enter your application name: ")
    app_root_directory = input("Specify loction of your app(or press Enter): ")
    if app_root_directory in ('', "\n"):
        app_root_directory = f"{os.getcwd()}/{project_name}"
    elif project_name not in ('', "\n"):
        app_root_directory = f"{os.getcwd()}/{app_root_directory}/{project_name}"
    root_path = pathlib.Path(app_root_directory).absolute()

    entrypoint(root_path, "example_project_structures/default.json")
    print(f"Folder structure created at: {root_path}")
