import sqlite3

name = "twitch_mod.py"
db = sqlite3.connect('../plugins/twitch/db_twitch.sqlite')


def buildup():
    print "This function is run at creation of the plugin"


def run(inp, sender, channel):
    #return sender + " This was your input " + inp

    ## Check for banned phrases

    ## Check for spam based on velocity

    ## Check for spam based on repeated phrases

    return ""


def desc():
    return "Helps moderate Twitch chat rooms."


def teardown():
    print "This function is run at removal of the plugin"
