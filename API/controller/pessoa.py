from fastapi import HTTPException
from sqlmodel import Session, select
from .generic import create_crud_router
from usuarioAPI1103.model.models import Pessoa
from usuarioAPI1103.model.dto import PessoaCreate, PessoaUpdate, PessoaRead

router = create_crud_router(
    model=Pessoa,
    create_schema=PessoaCreate,
    update_schema=PessoaUpdate,
    read_schema=PessoaRead,
    prefix="/pessoas",
    tags=["Pessoas"],
)
