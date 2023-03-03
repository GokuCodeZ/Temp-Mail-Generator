from mailgw_temporary_email import Email
from pystyle import Write, Colors
from colorama import Fore
import os
os.system("cls" or "clear")
Write.Print("""
  __  __          _____ _         _____ ______ _   _ ______ _____         _______ ____  _____  
 |  \/  |   /\   |_   _| |       / ____|  ____| \ | |  ____|  __ \     /\|__   __/ __ \|  __ \ 
 | \  / |  /  \    | | | |      | |  __| |__  |  \| | |__  | |__) |   /  \  | | | |  | | |__) |
 | |\/| | / /\ \   | | | |      | | |_ |  __| | . ` |  __| |  _  /   / /\ \ | | | |  | |  _  / 
 | |  | |/ ____ \ _| |_| |____  | |__| | |____| |\  | |____| | \ \  / ____ \| | | |__| | | \ \ 
 |_|  |_/_/    \_\_____|______|  \_____|______|_| \_|______|_|  \_\/_/    \_\_|  \____/|_|  \_\

                       
                            Made By ! ~ GoKuCodeZ🖤#7996
                  https://github.com/GokuCodeZ/Temp-Mail-Generator
""", Colors.blue_to_purple, interval=0.000)

def listener(message):
    print("\nFrom: " + message['from']['address'])
    print("\nRetention Date: " + message['retentionDate'])
    print("\nSubject: " + message['subject'])
    print("Content: " + message['text'] if message['text'] else message['html'])

test = Email()
test.register()
print(f"""
    Mail: {Fore.GREEN}{str(test.address)}{Fore.WHITE}
    Domain: {Fore.GREEN}{test.domain}{Fore.WHITE}
""")

# Start listening
test.start(listener)
print("\nWaiting for new emails...")
