import uvicorn

if __name__ == "__main__":
    uvicorn.run("fast_api_find_links.main:app", host="127.0.0.1", port=8081, reload=True)
