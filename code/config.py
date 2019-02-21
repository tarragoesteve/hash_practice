import json

class Config:
    
    get = {}

    @staticmethod
    def load():
        with open('../config.json') as f:
            Config.get = json.load(f)

    @staticmethod
    def get_attribute_or_default(obj, attribute, default):
        if attribute in obj:
            return obj[attribute]
        else:
            return default

    @staticmethod
    def get_algorithm_name(key):
        if key in Config.get and "algorithm" in Config.get[key]:
            return Config.get[key]["algorithm"]
        else:
            return key
        

        
    