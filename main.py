from fastapi import FastAPI, Request
from pydantic import BaseModel

import random

class IndexResponse(BaseModel):
    apiversion: str
    author: str = None
    color: str = None
    head: str = None
    tail: str = None


class StartResponse(BaseModel):
    start_response: str = "ok"


class MoveResponse(BaseModel):
    move: str
    shout: str = None


class EndResponse(BaseModel):
    end_response: str = "ok"


app = FastAPI()


@app.get("/", response_model=IndexResponse)
def index():
    return {
        "apiversion": "1",
        "author": "",  # TODO: Your Battlesnake Username
        "color": "#888888",  # TODO: Personalize
        "head": "default",  # TODO: Personalize
        "tail": "default",  # TODO: Personalize
    } 

@app.post("/start", response_model=StartResponse)
async def start(request: Request):
    data = await request.json()

    print("START")
    return {"start_response": "ok"}

@app.post("/move", response_model=MoveResponse)
async def move(request: Request):
    # This function is called on every turn of a game. It's how your snake decides where to move.
    # Valid moves are "up", "down", "left", or "right".
    data = await request.json()

    # Choose a random direction to move in
    possible_moves = ["up", "down", "left", "right"]
    move = random.choice(possible_moves)

    print(f"MOVE: {move}")
    return {"move": move}

@app.post("/end", response_model=EndResponse)
async def end(request: Request):
    # This function is called when a game your snake was in ends.
    # It's purely for informational purposes, you don't have to make any decisions here.
    data = await request.json()

    print("END")
    return {"end_response": "ok"}