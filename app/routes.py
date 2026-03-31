from fastapi import APIRouter
from app.models import GastoRequest, GastoResponse
from app.service import analisar_gastos

router = APIRouter()

@router.get("/")
def home():
    return {"message": "API de gastos rodando 🚀"}


@router.post("/analisar", response_model=GastoResponse)
def analisar(request: GastoRequest):
    resultado = analisar_gastos(request.texto)
    return resultado