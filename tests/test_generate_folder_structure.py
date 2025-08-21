import os
import pathlib
import shutil
from pyscaffold.services.generate_structure import generate_folder_structure


def test_empty_input_creates_single_dir():
    root_path = pathlib.Path("tmp/empty_app")
    
    if root_path.exists():
        shutil.rmtree(root_path)

    generate_folder_structure(root_path, [])
    assert root_path.exists()
    shutil.rmtree("tmp")


def test_create_nested_dir():
    root_path = pathlib.Path("tmp/my_app")
    structure = [{"app": [{"models": []}]}]
    
    if root_path.exists():
        shutil.rmtree(root_path)

    generate_folder_structure(root_path, structure)
    dir_path = root_path / "app" / "models"
    
    assert dir_path.exists()
    shutil.rmtree("tmp")


def test_create_file():
    root_path = pathlib.Path("tmp/my_app")
    structure = ["main.py"]
    
    if root_path.exists():
        shutil.rmtree(root_path)

    print(f"root_path: {root_path}")
    generate_folder_structure(root_path, structure)
    file_path = root_path / "main.py"
    
    assert file_path.is_file()
    shutil.rmtree("tmp")


def test_create_nested_dir_with_file():
    root_path = pathlib.Path("tmp/my_app")
    structure = [{"app": ["main.py"]}]

    if root_path.exists():
        shutil.rmtree(root_path)

    generate_folder_structure(root_path, structure)
    dir_path = root_path / "app"
    file_path = root_path / "app" / "main.py"
    
    assert dir_path.exists() and dir_path.is_dir()
    assert file_path.exists() and file_path.is_file()
    shutil.rmtree("tmp")
