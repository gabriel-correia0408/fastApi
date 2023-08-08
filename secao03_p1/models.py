from typing import Optional

from pydantic import BaseModel, validator

class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int # mais de 12
    horas: int # mais de 10
    
    #escolhendo campo a ser validade
    @validator('titulo')
    def validar_titulo(cls, value):
        palavras = value.split(' ')
        if len(palavras) < 3:
            raise ValueError('O titulo deve conter pelo menos três palavras')
        
        if value.islower():
            raise ValueError('O titulo deve ser em letra capitalizado')
        
        return value
    
cursos = [
    Curso(id=1, titulo='Programação para leigos', aulas=42, horas=50),
    Curso(id=2, titulo='Programação de  Algoritmos', aulas=30, horas=40)
]