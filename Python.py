import os

while True:
 print()
 ask=input("What can I do for you : ")
 ask=ask.lower()
 
 if ("run" in ask) or ("open" in ask) and ("notepad" in ask) or ("editor" in ask):
        os.system("notepad")
 elif ("run" in ask) or ("open" in ask) and (("chrome" in ask) or ("browser" in ask)):
        os.system("chrome")
 elif ("run" in ask) or ("open" in ask) and (("explorer" in ask) or ("file manager" in ask)):
        os.system("explorer")
 elif ("run" in ask) or ("open" in ask) and (("paint" in ask) or ("drawing" in ask) or ("whiteboard" in ask)):
        os.system("mspaint")
 elif ("exit" in ask) or ("quit" in ask):
        break
 else:
        print()
        print("Not Supported")