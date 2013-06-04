## This is an example file for how all IRC modules should be
## Name of the module, to be returned in desc()
import sqlite3
import sys
import plugins.load_temp as temp

db = sqlite3.connect('../plugins/twitch/questions.sqlite')
c = db.cursor()
name = "trivia.py"
t_file = "../plugins/twitch/temp/trivia.tmp"

def buildup():
    print "This function is run at buildup of function."

def run(inp, sender, channel):
    data = temp.load_temp(t_file)
    ans = ""
    if data["asked"] == "false":
        if inp == "trivia" and sender == "riotgradius":
            try:
                c.execute("select question,answer from questions order by random() limit 1")
                s = c.fetchone()
                data["answer"] = s[1]
                ans = s[0].encode('ascii', 'ignore')
                data["asked"] = "true"
                temp.save_temp(t_file, data)
            except:
                print "Error generating question:", sys.exc_info()
        return ans

    if data["asked"] == "true":
        if inp == str.lower(data['answer']):
            data["asked"] = "false"
            temp.save_temp(t_file, data)
            return "You are correct " + sender + "!"

    if inp == "stop trivia" and sender == "riotgradius":
        data["asked"] = "false"
        temp.save_temp(t_file, data)
        return "Ending this question."

    return ""

def desc():
    return ""

def teardown():
    print "This function is run at removal of the plugin"
