import yaml

class ConfigurationClass:
    def __init__(self, config_path, key = None):
        self.config_path = config_path
        self.key = key
        self.config = self.loadConfiguration()

    def loadConfiguration(self):
        try:
            with open(self.config_path, 'r') as file:
                config = yaml.safe_load(file)
                if self.key:
                    return config[self.key.upper()] if config is not None else {}
                else:
                    return config if config is not None else {}
        except FileNotFoundError:
            print("Config File not found")
            return {}

    def addItem(self, key, value):
        if key not in self.config:
            self.config[key] = value
            self.saveConfiguration()
            print(f"Added {key}: '{value}'")
            return True
        else:
            print(f"Key {key} already exists with value: {self.config[key]}")
            return False

    def deleteItem(self, key):
        if key in self.config:
            del self.config[key]
            self.saveConfiguration()
            print(f"Removed {key}")
            return True
        else:
            print(f"Key {key} not found")
            return False

    def updateItem(self, key, value):
        if key in self.config:
            self.config[key] = value
            self.saveConfiguration()
            print(f"Updated {key}: '{value}'")
            return True
        else:
            print(f"Key {key} not found")
            return False

    def saveConfiguration(self):
        try:
            with open(self.config_path, 'w') as file:
                yaml.safe_dump(self.config, file)
        except FileNotFoundError:
            print("Config File not found")

