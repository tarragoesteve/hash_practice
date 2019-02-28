import fileinput
import json
import time
from config import Config

class SolutionInterface:
    
    def __init__(self):
        # init code
        return

    def value(self):
        # return the cost of the solution
        raise Exception('Solution value needs to be implemented')

    def to_string(self):
        # return the plain string representation of the solution
        return json.dumps(vars(self))

    def save(self):
        toSave = self.to_string()
        with open("../outputs/%i_%i" % (self.value(), time.time()), "w") as text_file:
            text_file.write(toSave)

        withConfig = Config.json_string + '\n****\n' + toSave
        with open("../outputs_with_config/%i_%i" % (self.value(), time.time()), "w") as text_file:
            text_file.write(withConfig)

    def render(self):
        # pretty print of the solution
        return

    def validate(self):
        return True