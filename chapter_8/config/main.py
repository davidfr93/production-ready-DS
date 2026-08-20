import yaml
import pandas as pd




# Load config
with open("main.yaml", "r") as f_in:
    config = yaml.safe_load(f_in)

type(config)
config
config["data_path"]
config["data_path"]["raw"]
config["columns"]["to_drop"]
config["columns"]["target"]

data = pd.read_csv(config["data_path"]["raw"])
data = data.drop(columns=config["columns"]["to_drop"])
X = data.drop(columns=config["columns"]["target"])
y = data[config["columns"]["target"]]



import yaml
import os


!ls
# Load environment-specific config
env = os.getenv("ENVIRONMENT", "development")
env
with open(f"{env}.yaml", "r") as file:
    config = yaml.safe_load(file)

config
print(f"Using {env} environment")
print(f"Data source: {config['data_source']}")



