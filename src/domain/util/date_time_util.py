from datetime import datetime


class DateTimeUtil:
    default_date_format = "%Y-%m-%dT%H:%M:%S"

    @staticmethod
    def string_to_date(
        date_str: str, date_format: str = default_date_format
    ) -> datetime:
        return datetime.strptime(date_str, date_format)

    @staticmethod
    def date_to_iso_string(date: datetime) -> str:
        return date.isoformat()

    @staticmethod
    def date_to_string(date: datetime, date_format: str = default_date_format) -> str:
        return date.strftime(date_format)

    @staticmethod
    def is_valid_date(date: datetime) -> bool:
        try:
            if not isinstance(date, datetime):
                raise ValueError
            else:
                return True
        except ValueError:
            return False

    @staticmethod
    def is_valid_date_string(
        date_string: str, date_format: str = default_date_format
    ) -> bool:
        try:
            DateTimeUtil.string_to_date(date_string, date_format)
            return True
        except ValueError:
            return False
