# from AO3 import app

# if __name__ == "__main__":
#     import unicorn

#     uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)


from AO3 import app

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/works/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
