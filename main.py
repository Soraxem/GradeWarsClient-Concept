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



tree = ET.parse('Task1.xml')
root = tree.getroot()

demoTaskNow = 1;

loggedIn = False
username = ""
password = ""
key = ""

url = "http://beringen.odenwilusenz.ch:25577/GWS/test.php"
myobj = {'username': 'Johnn', 'password': 'Doe'}
#x = requests.post(url, data = myobj)
#print(x.text)

def loadTextTask():
    global tree
    global root
    text = ""
    for t in root.findall("text"): #add linebreaks
        text = text + t.text + "</br>"
    text = text[:-5:] #delete last Linebreak
    #Text Completed

    print(root.attrib["reply-type"])
    if (root.attrib["reply-type"] == "options"):
        print("Teel")
        table = "" #table init
        i = 0
        for options in root.findall("options"):
            table = table + "<tr>"
            for option in options.findall("option"):
                table = table + '<td onclick="eel.answer(' + str(i) +',1)">' + option.text + "</td>"
                i += 1

            table = table + "</tr>"
        #table completed
        eel.loadTextTaskOptions(text, table)

    elif (root.attrib["reply-type"] == "input"):
        if (root.attrib["input-type"] == "number"):
            eel.loadTextTaskNumber(text)
        elif (root.attrib["input-type"] == "text"):
            eel.loadTextTaskText(text)
        else:
            print("Error! ")
    else:
        print("Error! invlid XML Statement")


def loadImgTask():
    global tree
    global root
    text = ""
    for t in root.findall("text"): #add linebreaks
        text = text + t.text + "</br>"
    text = text[:-5:] #delete last Linebreak
    #Text Completed

    url = ""
    for t in root.findall("img"):
        url = t.text

    print(root.attrib["reply-type"])
    if (root.attrib["reply-type"] == "options"):
        print("Teel")
        table = "" #table init
        i = 0
        for options in root.findall("options"):
            table = table + "<tr>"
            for option in options.findall("option"):
                table = table + '<td onclick="eel.answer(' + str(i) +',1)">' + option.text + "</td>"
                i += 1

            table = table + "</tr>"
        #table completed
        eel.loadImgTaskOptions(text, table, url)

    elif (root.attrib["reply-type"] == "input"):
        if (root.attrib["input-type"] == "number"):
            eel.loadImgTaskNumber(text, url)
        elif (root.attrib["input-type"] == "text"):
            eel.loadImgTaskText(text, url)
        else:
            print("Error! ")
    else:
        print("Error! invlid XML Statement")
    

@eel.expose
def answer(value, form):
    demo()
    if(form == 1):
        print("taskformat" + str(form) + " awnsered:" + str(value) )
    elif (form == 2):
        print("taskformat" + str(form) + " awnsered:" + str(value) )

@eel.expose
def loginSubmit(user, passwordt, save):
    global loggedIn
    global username
    global password
    global key

    eel.showLoad()
    url = "http://beringen.odenwilusenz.ch:25577/GWS/test.php"
    myobj = {'username': user, 'password': passwordt}
    potKey = requests.post(url, data = myobj)
    print(potKey.text)
    if (potKey.text != "falseArgs"):
        key = potKey.text
        loggedIn = True
        username = user
        print("Logged in Succesfully!")
        if (save):
            password = passwordt
            eel.hideLoad()
            eel.hideLogin()
            demo()
    else:
        eel.hideLoad()
        print("Login Error!")
    
    
        
@eel.expose
def login():
    eel.showLogin()

def demo():
    global demoTaskNow
    load("Task" + str(demoTaskNow) + ".xml")
    if (demoTaskNow <= 5):
        demoTaskNow = demoTaskNow + 1
    else:
        demoTaskNow = 1

@eel.expose
def load(task):
    global tree
    global root
    tree = ET.parse(task)
    root = tree.getroot()
    if (root.tag != "task"):
        print("Error! False root argument -> it Has to be 'task' not: '" + root.tag + "'")
    else:
        if (root.attrib["type"] == "text"):
            loadTextTask()
        elif (root.attrib["type"] == "img"):
            loadImgTask()


# Set web files folder and optionally specify which file types to check for eel.expose()
eel.init('web', allowed_extensions=['.js', '.html'])
eel.start('index.html', mode='chrome')
