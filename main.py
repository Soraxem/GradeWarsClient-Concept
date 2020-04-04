import os
import platform
import sys
import time
import requests
import xml.etree.ElementTree as ET

# Use latest version of Eel from parent directory
sys.path.insert(1, '../../')
import eel

# Use the same static files as the original Example

# Set web files folder and optionally specify which file types to check for eel.expose()
eel.init('web', allowed_extensions=['.js', '.html'])

tree = ET.parse('Task1.xml')
root = tree.getroot()


url = "http://beringen.odenwilusenz.ch:25577/kak.php"
myobj = {'': 'Der Hannes'}
x = requests.post(url, data = myobj)
print(x.text)

def loadTaskFormat1():
    global tree
    global root
    text = ""
    for t in root.findall("text"): #add linebreaks
        text = text + t.text + "</br>"
    text = text[:-5:] #delete last Linebreak
    #Text Completed

    table = "" #table init
    i = 0
    for options in root.findall("options"):
        table = table + "<tr>"
        for option in options.findall("option"):
            table = table + '<td onclick="eel.answer(' + str(i) +',1)">' + option.text + "</td>"
            i += 1

        table = table + "</tr>"
    #table completed
    eel.loadTaskFormat1(text, table)

@eel.expose
def answer(value, form):
    print("taskformat" + str(form) + " awnsered:" + str(value) )


@eel.expose
def load():
    global tree
    global root
    tree = ET.parse('Task1.xml')
    root = tree.getroot()
    if (root.tag != "task"):
        print("Error! False root argument -> it Has to be 'task' not: '" + root.tag + "'")
    else:
        if (root.attrib["format"] == "1"):
            loadTaskFormat1()



eel.start('index.html', mode='chrome')
