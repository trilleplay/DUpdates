import requests
import random
import re
import json
import time

webhook_url = ""


def main():
    oldversion = check_for_updates_once()
    while True:
        time.sleep(random.choice([240, 260, 290, 310]))
        currentversion = check_for_updates()

        if oldversion == currentversion:
            print("No new update could be found.")
        else:
            url = webhook_url

            payload = "\n{\n    \"embeds\": [{\n        \"title\": \"New update available!\",\n        \"description\": \"A new update for canary just dropped! " + (currentversion) + "\",\n        \"color\": 15490563\n    }]\n}"
            headers = {
                'Content-Type': "application/json",
                'cache-control': "no-cache"
            }

            requests.request("POST", url, data=payload, headers=headers)
            oldversion = currentversion

def check_for_updates_once():
    url = "https://canary.discordapp.com/app"
    payload = ""
    headers = {
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, data=payload, headers=headers)
    matches = re.findall(r'(/assets/[\w.]+.js)', response.text, re.DOTALL)
    print(matches)

    for match in matches:
        try:
            print(match)
            url = "https://canary.discordapp.com" + (match)
            payload = ""
            headers = {
                'cache-control': "no-cache"
                }
            response = requests.request("GET", url, data=payload, headers=headers)
            buildversion = re.findall(r'(Build Number: \d{5})', response.text, re.DOTALL)

        except:
            print("The Build Number could not be identified.")

    print("Build Number found!")
    print(f'{buildversion}')
    updatev = json.dumps(buildversion)
    thing = (updatev[2] + updatev[3] + updatev[4] + updatev[5] + updatev[6] + updatev[7] + updatev[8] + updatev[9] + updatev[10] + updatev[11] + updatev[12] + updatev[13] + updatev[14] + updatev[15] + updatev[16] + updatev[17] + updatev[18] + updatev[19] + updatev[20])
    return(thing)

def check_for_updates():
    url = "https://canary.discordapp.com/app"
    payload = ""
    headers = {
        'cache-control': "no-cache"
        }

    response = requests.request("GET", url, data=payload, headers=headers)
    matches = re.findall(r'(/assets/[\w.]+.js)', response.text, re.DOTALL)
    print(matches)

    for match in matches:
        try:
            print(match)
            url = "https://canary.discordapp.com" + (match)
            payload = ""
            headers = {
                'cache-control': "no-cache"
                }
            response = requests.request("GET", url, data=payload, headers=headers)
            buildversion = re.findall(r'(Build Number: \d{5})', response.text, re.DOTALL)

        except:
            print("The Build Number could not be found.")

    print("Build Number found!")
    print(f'{buildversion}')
    updatev = json.dumps(buildversion)
    thing = (updatev[2] + updatev[3] + updatev[4] + updatev[5] + updatev[6] + updatev[7] + updatev[8] + updatev[9] + updatev[10] + updatev[11] + updatev[12] + updatev[13] + updatev[14] + updatev[15] + updatev[16] + updatev[17] + updatev[18] + updatev[19] + updatev[20])
    return(thing)


main()
