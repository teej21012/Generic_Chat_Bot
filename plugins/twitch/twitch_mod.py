## This is an example file for how all IRC modules should be

## Name of the module, to be returned in desc()
name = "Example.py"

## What the module should return when processing text from IRC
## Gets inp from IRC, processes it, and returns the
def buildup():
    print "This function is run at creation of the plugin"

def run(inp, sender, channel):
    #return sender + " This was your input " + inp
    return ""

## Returns a description of the module including the name at the top
def desc():
    return

def teardown():
    print "This function is run at removal of the plugin"
