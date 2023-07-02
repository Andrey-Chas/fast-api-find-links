from fastapi import FastAPI, Request
from fast_api_find_links.some_text import SomeText
from fast_api_find_links.find_meeting_links import *

app = FastAPI()

# links = []
# head = "http://127.0.0.1:8081/find_links"
# some_text = json.dumps({
#     "text": "Some text https://jf.je here where to find links from, https://google.com/"
# })
#
# request_find = requests.post(head, data=some_text)




@app.get("/")
async def root():
    return {"message": "Hello Wudpecker"}


@app.get("/find_links")
async def find_links(text: SomeText):
    links = []
    split_text = text.text.split()
    for word in split_text:
        if word.startswith("http:") or word.startswith("https:"):
            links.append(word)
    return links


@app.get("/find_meeting_links")
async def find_links(text: SomeText):
    meeting_links = []
    split_text = text.text.split()
    for word in split_text:
        match_link = find_link_method_1(word)
        if match_link != "":
            meeting_links.append(match_link)
    return meeting_links


@app.post("/get_calendar_events")
async def load_data(data: Request):
    data_to_load = await data.json()
    return data_to_load
