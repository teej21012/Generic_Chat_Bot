from lib.bot.ircBot import MessageLogger,GameBotFactory
from lib.game.markov import Markov
from twisted.python import log
from twisted.internet import reactor, protocol
import sys

log.startLogging(sys.stdout)
f = GameBotFactory("#testgradius", "swift.log")
reactor.connectTCP("irc.freenode.net", 6667, f)
reactor.run()
