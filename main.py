from fastapi import FastAPI
from pydantic import BaseModel
import json
from pathlib import Path

app = FastAPI()

ARQUIVO = Path("dados.json")

class Item(BaseModel):
    name: str

def read_json():
    if not ARQUIVO.exists():
        return []

    with open(ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)

def write_json(data):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

@app.get("/items")
def get_items():
    return read_json()

@app.post("/items")
def add_item(item : Item):
    data = read_json()
    data.append(item.name)
    write_json(data)
    return {"success": True, "item": item.name}

@app.delete("/items")
def remove_item(item : Item):
    data = read_json()
    data.remove(item.name)
    write_json(data)
    return{"sucess": True}