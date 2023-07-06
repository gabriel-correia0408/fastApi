from typing import Optional

from pydantic import BaseModel

class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int
    
cursos = [
    Curso(id=1, titulo='Programação para leigos', aulas=42, horas=50),
    Curso(id=2, titulo='Programação Algoritmos', aulas=30, horas=40)
]