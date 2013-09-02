Generic_Chat_Bot
================

Generic chat libraries for creating bots for various services.

Notes
================

Starting this project over with a bit more organization in mind.  Here's the general direction...

The project will consist of these pieces:
 
 * Connectors - Used to connect to chat services.  Will recieve input, send output, and load plugins.  Will provide the plugins with a callback function to send messages at any point
  
 * Libraries - Support the Connectors and Plugins.  Will contain the plugin loader and the permissions library at the moment,
  
 * Plugins - Different functions the chat bot can perform.  The connector iterates through the current list of plugins and send each plugin the user input.  Makes use of the permissions library
