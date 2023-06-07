import requests
import json

def find_links():
    links = []
    url = "http://127.0.0.1:8081/findlinks"

    body = json.dumps({
        "text": "Some text https://jf.je here where to find links from, https://google.com/"
    })

    response = requests.post(url, data=body)

    splitted = response.split()

    for word in splitted:
        if word.startswith("https:") or word.startswith("http:"):
            links.append(word)

    return links
