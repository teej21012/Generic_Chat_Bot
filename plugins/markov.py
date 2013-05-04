## This is an example file for how all IRC modules should be

## Name of the module, to be returned in desc()
name = "markov.py"

## What the module should return when processing text from IRC
## Gets inp from IRC, processes it, and returns the
def run(inp, sender, channel):
    return sender + " This was your input " + inp

## Returns a description of the module including the name at the top
def desc():
    return "Module name" + name + ":chains phrases it knows together to make AWESOME sentences."

class Markov():

    def __init__(self):
        print ""
