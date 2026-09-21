
import yaml


with open(
    "config/env.yaml",
    encoding="utf-8"
) as f:

    config = yaml.safe_load(f)



ENV = "dev"


BASE_URL = config[ENV]["base_url"]