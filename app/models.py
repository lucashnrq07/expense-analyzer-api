from pydantic import BaseModel
from typing import Dict, List

class GastoRequest(BaseModel):
    texto: str

class GastoResponse(BaseModel):
    total: float
    categorias: Dict[str, float]
    erros: List[str]