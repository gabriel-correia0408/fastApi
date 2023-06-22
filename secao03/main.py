from fastapi import FastAPI

app = FastAPI()

cursos = {
    1: {
        "titulo": "Programação para leigos",
        "aulas": 122,
        "horas": 58
        },
    2: {
        "titulo": "Algoritmos de programação",
        "aulas": 87,
        "horas": 67
        }
}



if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000)