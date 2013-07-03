## This is an example file for how all IRC modules should be
import aiml
import sys

## Name of the module, to be returned in desc()
name = "markov.py"
kernel = aiml.Kernel()
kernel.learn("../plugins/aiml_brains/load_standard.xml")
## Link to AIML Brains
## http://code.google.com/p/aiml-en-us-foundation-alice/downloads/list

## What the module should return when processing text from IRC
## Gets inp from IRC, processes it, and returns the
def buildup():
    print ""

def run(inp, sender, channel):
    reply = kernel.respond(inp)

    return reply


## Returns a description of the module including the name at the top
def desc():
    return "Module name" + name + ":chains phrases it knows together to make AWESOME sentences."

def teardown():
    print ""
