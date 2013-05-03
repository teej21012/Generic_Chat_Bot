## ircutils documentation: http://dev.guardedcode.com/docs/ircutils/py-modindex.html
from ircutils import client
import ConfigParser


class IrcBot():

    def __init__(self, config_file):
        #Parse Configuration File
        config = ConfigParser.RawConfigParser()
        config.read(config_file)

        #Obtain Configuration Vaules
        self.server = config.get('Settings', 'server')
        self.port = int(config.get('Settings', 'port'))
        self.nick = config.get('Settings', 'nick')
        self.username = config.get('Settings', 'username')
        self.password = config.get('Settings', 'password')
        self.owner = config.get('Settings', 'owner')

        channels_string = config.get('Settings', 'channels')
        self.channels = list(filter(None, (x.strip() for x in channels_string.splitlines())))

        self.bot = client.SimpleClient(nick = self.nick)

    def message_printer(self, event):
        print "<{0}/{1}> {2}".format(event.source, event.target, event.message)

    def notice_printer(self, client, event):
        print "(NOTICE) {0}".format(event.message)

    def welcome_message(self,event):
        print "OMG WELCOME"

    def bot_start(self):
        self.bot["welcome"].add_handler(self.welcome_message)
        self.bot["notice"].add_handler(self.notice_printer)
        self.bot.connect(self.server, self.port)
        self.bot.start()
