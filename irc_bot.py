from connectors.irc import IrcBot

irc = IrcBot("configs/irc_config.cfg")
irc.bot_start()
