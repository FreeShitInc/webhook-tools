import requests,json
from time import sleep


banner ="""
███████╗██████╗ ███████╗███████╗███████╗██╗  ██╗██╗████████╗
██╔════╝██╔══██╗██╔════╝██╔════╝██╔════╝██║  ██║██║╚══██╔══╝  
█████╗  ██████╔╝█████╗  █████╗  ███████╗███████║██║   ██║      
██╔══╝  ██╔══██╗██╔══╝  ██╔══╝  ╚════██║██╔══██║██║   ██║    
██║     ██║  ██║███████╗███████╗███████║██║  ██║██║   ██║     
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝   ╚═╝    
Created By FreeShit ║ Developer: segations#2344 ║getfreeshit.today
"""

def main():
    print(banner)
    print("""
[S] Spammer
[D] Deleter
[C] Status Checker + Info""")
    
    wow = input("-> ")
    if wow == "s" or wow == "S":
        spammer()
    if wow == "d" or wow == "D":
        deleter()
    if wow == "c" or wow == "C":
        status()
    else: 
        print("Not Valid Input")
        
def spammer():
    print(banner)
    headers = {
    'Content-Type': 'application/json'
    }
    print("You Selected Module Spammer!")
    Webhook = input("Webhook: ")
    username = input("Username: ")
    message = input("Message: ")
    amount = input("Amount: ")
    payload = json.dumps({
        "username": username,
        "content": message
    })
    for x in range(int(amount)):
        r = requests.post(Webhook,headers=headers, data=payload)
        if r.status_code == 204:
            print("Sent Message Successfully")
        if r.status_code == 429:
            print("Discord Did a RateLimit - " + str(r.json()["retry_after"]))
            sleep(r.json()["retry_after"])
    main()

def deleter():
    print(banner)
    print("You Selected Module Deleter!")
    Webhook = input("Webhook: ")
    r = requests.delete(Webhook)
    print(Webhook + " - " + str(r.status_code))
    main()

def status():
    print(banner)
    print("You Selected Module Status + Info!")
    Webhook = input("Webhook: ")
    r = requests.get(Webhook)
    if r.status_code == 404:
        print(f"The url ({Webhook}) you inputted status code is 404")
    elif r.status_code == 200:
        print("""
Here is the Info:
ID: {}
Name: {}
Channel_ID: {}
Guild_ID: {}
Application_ID: {}
Token: {}
""".format(r.json()["id"], r.json()["name"], r.json()["channel_id"], r.json()["guild_id"], r.json()["application_id"], r.json()["token"]))
    main()



if __name__ == "__main__":
    main()
