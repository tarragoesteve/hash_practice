import json

class Config:
    
    get = {}

    @staticmethod
    def load():
        with open('../config.json') as f:
            Config.get = json.load(f)

    @staticmethod
    def getAttributeOrDefault(obj, attribute, default):
        if attribute in obj:
            return obj[attribute]
        else:
            return default

    @staticmethod
    def getAlgorithmName(key):
        if key in Config.get and "algorithm" in Config.get[key]:
            return Config.get[key]["algorithm"]
        else:
            return key
        

        
    