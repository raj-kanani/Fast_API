# from fastapi import FastAPI
#
# app = FastAPI() # create fast API instance.
#
#
# @app.get('/status/{name}')
# async def status(name):
#     return {"message": f'fast api testing : {name}'}
#

from fastapi import FastAPI

app = FastAPI()  # create fast API instance.
food = {
    'indian': ['Samosa', "Dosa"],
    'america': ['Hot Dog', 'Pizza'],

}

@app.get('/items/{name}')
async def status(name):
    return food.get(name)
