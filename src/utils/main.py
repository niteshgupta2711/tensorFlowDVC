import yaml
def read_yaml(path: str) -> dict:
    with open(path) as yaml_file:
        content=yaml.safe_load(yaml_file)
    return content
