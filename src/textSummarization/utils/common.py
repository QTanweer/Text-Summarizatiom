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
    """
    Reads a yaml file and returns a ConfigBox object

    Args:
        path_to_yaml (Path): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty yaml file

    Returns:
        ConfigBox: ConfigBox object
    """

    # print(f"Inside read_yaml func before try clase:{path_to_yaml},and type: {type(path_to_yaml)}")

    # print(os.path.exists(path_to_yaml))

    try:
        # print(f"Inside read_yaml function's try: {path_to_yaml}, and type: {type(path_to_yaml)}")
        with open(path_to_yaml, "r", encoding='utf-8') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info("yaml file: %s loaded successfully", path_to_yaml)
            config = ConfigBox(content)
            return config
    except BoxValueError as exc:
        print(f"Inside read_yaml function's except: {path_to_yaml} is empty")
        raise ValueError('Empty yaml file') from exc
    except Exception as ex:
        raise ex


# @ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Creates directories

    Args:
        path_to_directories (list): list of directories to create
    """
    for dir_path in path_to_directories:
        os.makedirs(dir_path, exist_ok=True)
        logger.info("directory: %s created successfully", dir_path)
        if verbose:
            logger.info("directory: %s created successfully", dir_path)


def get_size(path: Path):
    """
    Gets size of a file in KB

    Args:
        path (Path): path like input to file

    Returns:
        Any: size of file
    """
    size = f"~ {round(os.path.getsize(path) / 1024, 2)} KB"
    logger.info("file: %s size: %s", path, size)
    return size

