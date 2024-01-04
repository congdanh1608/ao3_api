# Trong file main.py
# from AO3 import app
from ao3_api import AO3

if __name__ == "__main__":
    import unicorn

    uvicorn.run(AO3, host="0.0.0.0", port=8000, reload=True)
