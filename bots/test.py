"""
from irc_bot import IrcBot

bot = IrcBot("configs/irc_config.cfg")
bot.bot_start()
"""
from ircutils import client

def message_printer(client, event):
    print "<{0}/{1}> {2}".format(event.source, event.target, event.message)

def notice_printer(client, event):
    print "(NOTICE) {0}".format(event.message)

def on_welcome(client, event):
    my_client.join("#testgradius")

# Create a SimpleClient instance
my_client = client.SimpleClient(nick="girldius")
my_client.real_name = "Test"
my_client.user = "Test"
# Add the event handlers
my_client["welcome"].add_handler(on_welcome)
my_client["channel_message"].add_handler(message_printer)
my_client["notice"].add_handler(notice_printer)

# Finish setting up the client
my_client.connect("irc.freenode.com", channel="#testgradius")
my_client.start()
