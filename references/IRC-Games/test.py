from lib.bot.ircBot import MessageLogger,GameBotFactory
from lib.game.markov import Markov
from twisted.python import log
from twisted.internet import reactor, protocol
import sys


m = Markov(2)
"""
m.add("This is a test sentence.")
m.add("This is a cat sentence.")
m.add("a cat is not friendly")
m.add("tom is never home")
m.add("tom cant go home when it is on fire")
"""
f=open("seeds/book1.txt")
for line in f:
    m.add(line)
f=open("seeds/file.txt")
for line in f:
    m.add(line)
print m.generate("too much to say how much you can do",20)

#print m.find_chain("cat")