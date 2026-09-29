from typing import Optional

from fastapi import Cookie, FastAPI

app = FastAPI()


@app.get("/chatbot")
def conversar(session_id: Optional[str] = Cookie(None)):
    if session_id:
        return {
            "status": "Sessão ativa",
            "historico_conversado": "Lembrando do contexto anterior...",
        }
    return {"status": "Nova sessão", "mensagem": "Por favor, inicie uma conversa."}
