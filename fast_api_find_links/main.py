from fastapi import FastAPI
from fast_api_find_links.some_text import SomeText

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
