from fastapi import FastAPI

# variavel {app} vai carregar o FastAPI
app = FastAPI()


@app.get('/mensagem')
async def raiz():
    return {"msg": "FastAPi"}



if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info", reload=True)