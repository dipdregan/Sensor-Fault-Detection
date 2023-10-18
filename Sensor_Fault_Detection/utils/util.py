from Sensor_Fault_Detection.exception import SensorException
from Sensor_Fault_Detection.logger import logging
import sys
import os
import yaml
import numpy as np
import dill

def read_yaml_file(file_path: str) -> dict:
    """
    Reads a YAML file and returns its contents as a dictionary.

    Args:
        file_path (str): The path to the YAML file to be read.

    Returns:
        dict: A dictionary containing the YAML file's contents.

    Raises:
        SensorException: If any exceptions occur during file reading.

    """
    try:
        with open(file_path, 'rb') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logging.info(f"Read YAML file: {file_path}")
            return content
    except Exception as e:
        logging.error(f"Error reading YAML file {file_path}: {str(e)}")
        raise SensorException(e, sys)

def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    """
    Writes content to a YAML file at the specified file path.

    Args:
        file_path (str): The path to the YAML file to be written.
        content (object): The content to be written to the YAML file.
        replace (bool, optional): If True, the existing file at file_path will be replaced. Defaults to False.

    Raises:
        SensorException: If any exceptions occur during file writing.

    """
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, 'w') as file:
            yaml.dump(content, file)
        logging.info(f"Write YAML file: {file_path}")
    except Exception as e:
        logging.error(f"Error writing to YAML file {file_path}: {str(e)}")
        raise SensorException(e, sys)

def save_numpy_data(file_path: str, array: np.array):
    """
    Saves a NumPy array to a binary file at the specified file path.

    Args:
        file_path (str): The path to the binary file where the array will be saved.
        array (np.array): The NumPy array to be saved.

    Raises:
        SensorException: If any exceptions occur during file writing.

    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            np.save(file_obj, array)
        logging.info(f"Save NumPy array to file: {file_path}")
    except Exception as e:
        logging.error(f"Error saving NumPy array to file {file_path}: {str(e)}")
        raise SensorException(e, sys)

def save_object(file_path: str, obj: object):
    """
    Saves an object to a binary file at the specified file path using dill.

    Args:
        file_path (str): The path to the binary file where the object will be saved.
        obj (object): The object to be saved.

    Raises:
        SensorException: If any exceptions occur during file writing.

    """
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
        logging.info(f"Save object to file: {file_path}")
    except Exception as e:
        logging.error(f"Error saving object to file {file_path}: {str(e)}")
        raise SensorException(e, sys)

def load_object(file_path: str,)->object:

    try:
        if not os.path.exists(file_path):
            raise Exception(f"File path :{file_path} is not exits")

        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "rb") as file_obj:
            dill.load(file_obj)
            return dill
        
    except Exception as e:
        raise SensorException(e, sys)


def load_numpy_array_data(file_path: str) -> np.array:
    """
    Loads a NumPy array from a binary file at the specified file path.

    Args:
        file_path (str): The path to the binary file containing the NumPy array.

    Returns:
        np.array: The NumPy array loaded from the file.

    Raises:
        SensorException: If any exceptions occur during file reading.

    """
    try:
        with open(file_path, 'rb') as file_obj:
            array_data = np.load(file_obj)
            logging.info(f"Loaded NumPy array from file: {file_path}")
            return array_data
    except Exception as e:
        logging.error(f"Error loading NumPy array from file {file_path}: {str(e)}")
        raise SensorException(e, sys)
