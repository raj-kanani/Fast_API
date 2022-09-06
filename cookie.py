from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


@app.post("/cookie/")
def create_cookie():
    content = {"message": "Come to the cookies testing"}
    response = JSONResponse(content=content)
    response.set_cookie(key="wrong-session", value="fake-cookie-session-value")
    return response
