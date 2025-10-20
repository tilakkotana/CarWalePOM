from configparser import ConfigParser
from pathlib import Path


def read_config(section,value):
    config=ConfigParser()
    file_path = Path.cwd().parent / 'ConfigurationData/config.ini'
    config.read(file_path)
    return config.get(section,value)