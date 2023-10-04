'''
common utilitiies
'''
import os
from pathlib import Path
from typing import Any
import yaml
from ensure import ensure_annotations
import box
from box import ConfigBox
from box import exceptions
from box.exceptions import BoxValueError
from textSummarization.logging import logger



@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads yaml file

    Args:
        path_to_yaml (str): path like input

    Raises:
        BoxValueError: If yaml file is empty
        e: empty yaml file

    Returns:
        ConfigBox: ConfigBox object
    """
    try:
        with open(path_to_yaml, encoding='utf-8') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info("Loaded yaml file: %s", path_to_yaml)
            return ConfigBox(content)
    except BoxValueError as exc:
        raise BoxValueError("Empty yaml file") from exc
    except Exception as error:
        raise error


@ensure_annotations
def create_directories(path_to_directories: list, verbose = True) :
    """Create list of directories

    Args:
        path_to_directories (list): list of path of directories
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info("Created directory: %s", path)


@ensure_annotations
def get_size(path: Path) -> str:
    """Get size of file in KB

    Args:
        path (Path): path of file

    Returns:
        str: size of KB
    """

    return f"~{(os.path.getsize(path)/1024):.2f} KB"
