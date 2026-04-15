from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

app = FastAPI()

# Libera acesso do frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelo de item
class Item(BaseModel):
    descricao: str
    quantidade: int
    valor_unitario: float

# Modelo de fatura
class Fatura(BaseModel):
    cliente: str
    itens: list[Item]
    imposto: float = 0

# Rota inicial
@app.get("/")
def home():
    return {"status": "API rodando"}

# Criar fatura
@app.post("/fatura")
def criar_fatura(fatura: Fatura):
    total_produtos = sum(item.quantidade * item.valor_unitario for item in fatura.itens)
    total_imposto = total_produtos * (fatura.imposto / 100)
    total_geral = total_produtos + total_imposto

    return {
        "cliente": fatura.cliente,
        "data": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "total_produtos": total_produtos,
        "imposto_percentual": fatura.imposto,
        "valor_imposto": total_imposto,
        "total_final": total_geral,
        "itens": fatura.itens
    }