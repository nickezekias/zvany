from fastapi import HTTPException, status

from src.domain.base.i_presenter import IPresenter


class Presenter(IPresenter):
    def output(self, data: object) -> object:
        pass

    def output_error_server_db_commit(self, details: str | None = None) -> None:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={
                "message": "server.errors.db.couldNotCommitToDB",
                "details": details,
            },
        )

    def output_error_domain_validation(self, details: dict | str) -> None:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(details)
        )

    def output_error_object_not_found(self, details: dict | str) -> None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail={str(details)}
        )
