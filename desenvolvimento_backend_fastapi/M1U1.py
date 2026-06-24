import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/user/{id}")
def get_user(id: int):
    return {"mensagem": f"Id fornecido: {id}"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=3000)
