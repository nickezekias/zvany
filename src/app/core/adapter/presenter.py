from abc import ABC
from typing import TypeVar
from fastapi import HTTPException, status
import json

from src.domain.base.i_presenter import IPresenter
I = TypeVar('I')
O = TypeVar('O')

class Presenter(IPresenter):
  def output(self, data: I) -> O:
    return super().output(data)

  def output_errors_sever_db_commit(self, details: str | None = None) -> None:
    raise HTTPException(
      status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
      detail={ "message": "server.errors.db.couldNotCommitToDB", "details": details }
    )
  
  def output_error_domain_validation(self, details: dict) -> None:
    raise HTTPException(
      status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
      detail=str(details)
    )