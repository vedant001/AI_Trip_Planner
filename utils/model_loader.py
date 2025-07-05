class ConfigLoader:
    def __init__(self, config_path):
        self.config_path = config_path


class ModelLoader(BaseModel):
    def __init__(self, config_loader: ConfigLoader):
        self.config_loader = config_loader


    