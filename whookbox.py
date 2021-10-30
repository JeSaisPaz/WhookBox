import os
from dhooks import Webhook
import urllib.request

hook = Webhook(input("webhook link (ALL THE LINK) > "))

def modify():
    options = input("modify - name or avatar > ")
    if options == "name":
        newname = input("Insert new name > ")
        hook.modify(str(newname))
        
    elif options == "avatar":
        newavatar = input("input new avatar URL (ONLY PNG's) > ")
        urllib.request.urlretrieve(newavatar, "newavatar")

        with open('newavatar', "rb") as f:
            img = f.read()

        hook.modify(avatar=img)

def getinfo():
    info = hook.get_info()
    print(info)

def spameveryone():
    everyone = "@everyone"
    while True:
        hook.send(everyone)

def customspam():
    hook.username = input("webhook username > ")
    hook.avatar_url = input("webhook avatar (url) > ")
    spammedmessage = input("message to spam > ")
    while True:
        hook.send(spammedmessage)

print("""
-----Welcome to WhookBox-----
   Made by JeSaisPas#0069
   Education purpose only
      Made with love
     to start type "help"
-----------------------------
    """)
while True:
    mainmenu = input("dhookbox_cmd > ")
    if mainmenu == "help":
        print("""
-----------------help command------------------
spam - spam the webhook with custom message
customspam - spam with custom name, etc...
spameveryone - spam @everyone on the server
delete - delete the webhook
getinfo - get the webhook info
exit - exit the program
clear - clear the terminal
----------------------------------------------
        """)
    elif mainmenu == "spameveryone":
        spameveryone()

    elif mainmenu == "delete":
        print("The Webhook has been Whooked")
        hook.delete()

    elif mainmenu == "customspam":
        customspam()

    elif mainmenu == "clear":
        os.system("cls")

    elif mainmenu == "getinfo":
        getinfo()

    elif mainmenu == "exit":
        quit()

    elif mainmenu == "modify":
        modify()

    else:
        print("ERROR: Not an option")