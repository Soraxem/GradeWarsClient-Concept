import os
import platform
import sys
import xml.etree.ElementTree as ET

# Use latest version of Eel from parent directory
sys.path.insert(1, '../../')
import eel

# Use the same static files as the original Example

# Set web files folder and optionally specify which file types to check for eel.expose()
eel.init('web', allowed_extensions=['.js', '.html'])

tree = ET.parse('Task1.xml')
root = tree.getroot()

def loadTaskFormat1():
    if (root.attrib["values"] == "static"):
        text = ""
        for t in root.findall("text"): #add linebreaks
            text = text + t.text + "</br>"
        text = text[:-5:] #delete last Linebreak
        #Text Completed

        table = "" #table init
        for options in root.findall("options"):
            table = table + "<tr>"
            for option in options.findall("option"):
                table = table + "<td>" + option.text + "</td>"

            table = table + "</tr>"
        #table completed
        print("Test")
        eel.loadTaskFormat1(text, table)

@eel.expose
def load():
    tree = ET.parse('Task1.xml')
    root = tree.getroot()
    if (root.tag != "task"):
        print("Error! False root argument -> it Has to be 'task' not: '" + root.tag + "'")
    else:
        if (root.attrib["format"] == "1"):
            loadTaskFormat1()



eel.start('index.html', mode='chrome')







# # Launching Edge can also be gracefully handled as a fall back
# try:
#     eel.start('hello.html', mode='chrome-app', size=(300, 200))
# except EnvironmentError:
#     # If Chrome isn't found, fallback to Microsoft Edge on Win10 or greater
#     if sys.platform in ['win32', 'win64'] and int(platform.release()) >= 10:
#         eel.start('hello.html', mode='edge')
#     else:
#         raise
