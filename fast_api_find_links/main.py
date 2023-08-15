from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fast_api_find_links.some_text import SomeText
from fast_api_find_links.find_meeting_links import *

app = FastAPI()

database = []

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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


@app.get("/get_calendar_events")
async def load_data():
    file_path = f"C:/Users/Andru/source/repos/User-Calendar/User-Calendar/wwwroot/data.json"
    return FileResponse(file_path)


@app.get("/post_data")
async def get_data():
    for item in database:
        return item
    return {"error": "Data not found"}


@app.post("/post_data")
async def add_data(data: dict):
    database.clear()
    database.append(data)
    return {"message": "Data published successfully"}
