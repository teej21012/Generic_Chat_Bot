## ircutils documentation: http://dev.guardedcode.com/docs/ircutils/py-modindex.html
from ircutils import client
import ConfigParser
from plugins.irc_loader import IrcLoader
import sys


class IrcBot(client.SimpleClient):

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
        self.channels_join = list(filter(None, (x.strip() for x in channels_string.splitlines())))

        plugin_string = config.get('Settings', 'plugins')
        self.plugins = list(filter(None, (x.strip() for x in plugin_string.splitlines())))

        self.mod_loader = IrcLoader()

        client.SimpleClient.__init__(self, self.nick)

    def message_printer(self, client, event):
        print "<{0}/{1}> {2}".format(event.source, event.target, event.message)

    def run_mods(self, client, event):
        for mod in self.mod_loader.listMods():
            try:
                msg = self.mod_loader.run(mod, event.message, event.source, event.target)
                self.send_message(event.target, msg)
            except:
                print "Error running mod:", sys.exc_info()

    def message_handler(self, client, event):

        ## Check for Admin commands
        if event.message[0] == "@" and event.source == self.owner:
            split = event.message.split()
            cmd = split[0]
            arg = split[1]

            if cmd == "@load":
                self.mod_loader.load(arg)

    def notice_printer(self, client, event):
        print "(NOTICE) {0}".format(event.message)

    def welcome_message(self,client,event):
        for chan in self.channels_join:
            self.join(chan)

    def bot_start(self):
        self["welcome"].add_handler(self.welcome_message)
        self["notice"].add_handler(self.notice_printer)
        self["message"].add_handler(self.message_printer)
        self["message"].add_handler(self.message_handler)
        self["message"].add_handler(self.run_mods)
        self.connect(self.server, self.port, password=self.password)
        self.start()
