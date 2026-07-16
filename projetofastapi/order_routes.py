from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import pegar_sessao, verificar_token
from schemas import PedidosSchema
from models import Pedido

order_router = APIRouter(prefix="/pedidos", tags=["pedidos"], dependencies=[Depends(verificar_token)])

@order_router.get("/")
async def pedidos():
    return {"mensagem": "Você acessou a rota de pedidos"}

@order_router.post("/pedido")
async def criar_pedido(pedido_schema: PedidosSchema, session: Session = Depends(pegar_sessao)):
    novo_pedido = Pedido(usuario=pedido_schema.usuario)
    session.add(novo_pedido)
    session.commit()
    return {"mensagem": f"Pedido criado com sucesso. ID do pedido {novo_pedido.id}"}

@order_router.post("/pedido/cancelar/{id_pedido}")
async def cacelar_pedido(id_pedido: int, session: Session = Depends(pegar_sessao)):
    pedido = session.query(Pedido).filter(Pedido.id==id_pedido).first()
    if not pedido:
        raise HTTPException(status_code=400, detail="Pedido não encontrado")
    pedido.status = "CANCELADO"
    session.commit()
    return {
        "mensagem": f"Pedido número: {id_pedido} cancelado com sucesso",
        "pedido": pedido
    }

