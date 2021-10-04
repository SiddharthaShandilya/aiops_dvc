import yaml
import os
import json

def read_yaml(path_to_yaml: str ) -> dict:
    with open( path_to_yaml) as yaml_file:
        content = yaml.safe_load(yaml_file)

    return content

def create_dictionary(dirs: list):
    for dir_path in dirs:
        os.makedirs(dir_path, exist_ok = True)
        print(f"directory is created at path : {dir_path}")

def save_local_df(data, dir_path, index_status=False):
    data.to_csv(dir_path, index = index_status)
    print(" Data is saved at () ".format(dir_path))
