import logging
from enum import Enum

from fastapi import FastAPI, Path, Body, Query
from pydantic import BaseModel, Field
import datetime as dt
import decimal as dec
from typing import Any, Optional, Union

BASE = "/simulador/"

app = FastAPI()


class Simulador(BaseModel):
    date: dt.datetime = Field(..., title="Data de Geracao do Arquivo")
    model: str = Field(..., title="Modelo do Trafo?")
    version: str | None = Field(
        None, title="Versao do gerador?"
    )  # Field(...) = obrigatorio / Field(None) = opcional
    values: dict[int, dec.Decimal] = Field(..., title="Valores")

    class Config:
        schema_extra = {
            "example": {
                "date": dt.datetime(2021, 12, 31, 13, 14, 15),
                "model": "Modelo abc",
                "version": "Versao xyz",
                "values": {0: dec.Decimal(1.33), 1: dec.Decimal(2.66)},
            }
        }


class BasicStatus(Enum):
    """Status de retorno da API."""

    success = "success"
    failure = "failure"


class BasicResponse(BaseModel):
    status: BasicStatus = Field(..., title="Status do servico")
    reason: str | None = Field(None, title="Motivo do status")

    class Config:
        schema_extra = {
            "example": {
                "status": BasicStatus.failure,
                "reason": "Problema interno",
            }
        }


@app.post(
    BASE + "ler_dados", response_model=BasicResponse, response_model_exclude_unset=True
)  # Método [get/post/delete/update]
async def nome_do_endpoint(simulador: Simulador) -> BasicResponse:
    """Breve descrição do endpoint contendo para que serve.

    Breve descricao de Quais são os Dados de entrada (Opicional).

    Breve descricao de Qual é a Saida.
    """
    print("\n", simulador.dict(), "\n")
    return BasicResponse(status=BasicStatus.success)
