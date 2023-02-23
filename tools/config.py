import yaml

yml_configs = None
with open('config.yml', 'r') as yml_file:
    yml_configs = yaml.safe_load(yml_file)
