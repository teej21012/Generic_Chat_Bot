## Name of the module, to be returned in desc()
name = "topic_changer.py"


def buildup():
    print "This function is run at creation of the plugin"


def run(inp, sender, channel):
    #return sender + " This was your input " + inp
    return ""


def desc():
    return "Changes Twitch channel title based on current LoL game"


def teardown():
    print "This function is run at removal of the plugin"
