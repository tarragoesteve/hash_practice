import fileinput
import json
import time

class SolutionInterface:
    
    def __init__(self):
        # init code
        return

    def value(self):
        # return the cost of the solution
        return 0

    def toString(self):
        # return the plain string representation of the solution
        return json.dumps(vars(self))

    def save(self):
        toSave = self.toString()
        with open("../outputs/%i_%i" % (self.value(), time.time()), "w") as text_file:
            text_file.write(toSave)

    def render(self):
        # pretty print of the solution
        return

    def validate(self):
        return True