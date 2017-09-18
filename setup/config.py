import os
import yaml
from configurate import Configurate

file_path = os.path.dirname(os.path.abspath(__file__))
project_path = os.path.abspath(os.path.join(file_path, os.path.pardir))
yml_path = os.path.join(project_path, 'setup/config.yml')

config = Configurate()

with open(yml_path, 'r') as config_file:
    config.merge(yaml.safe_load(config_file))