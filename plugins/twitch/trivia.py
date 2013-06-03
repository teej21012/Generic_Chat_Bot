## This is an example file for how all IRC modules should be

## Name of the module, to be returned in desc()
name = "trivia.py"

def buildup():
    print "This function is run at creation of the plugin"

def run(inp, sender, channel):
    return ""

def desc():
    return ""

def teardown():
    print "This function is run at removal of the plugin"
