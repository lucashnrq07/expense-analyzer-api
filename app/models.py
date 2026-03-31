from pydantic import BaseModel
from typing import Dict, List, Tuple

class GastoRequest(BaseModel):
    texto: str

class GastoResponse(BaseModel):
    total: float
    categorias: Dict[str, float]
    ranking: List[Tuple[str, float]]
    erros: List[str]