import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

import random

class BoardData(BaseModel):
    game: dict = None
    turn: int = None
    board: dict = None
    you: dict = None

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

@app.get("/start")
def read_start(board_data: BoardData):
    data = board_data

@app.post("/start", response_model=StartResponse)
def return_start(board_data: BoardData):
    data = board_data

    print("START")
    return {"start_response": "ok"}

@app.post("/move", response_model=MoveResponse)
def move(board_data: BoardData):
    data = board_data

    # Choose a random direction to move in
    possible_moves = ["up", "down", "left", "right"]
    move = random.choice(possible_moves)

    print(f"MOVE: {move}")
    return {"move": move}

@app.post("/end", response_model=EndResponse)
def end(board_data: BoardData):
    data = board_data

    print("END")
    return {"end_response": "ok"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)