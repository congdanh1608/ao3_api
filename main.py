# from AO3 import app

# if __name__ == "__main__":
#     import unicorn

#     uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)


from AO3 import works

@works.get("/works/{workid}")
def work(workid: int):
    return {"workid": workid}
