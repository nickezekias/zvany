from datetime import datetime, date

class DateTimeUtil:

    default_format = '%Y-%m-%dT%H:%M:%S'

    @staticmethod
    def string_to_date(date_str: str, format: str = default_format) -> datetime:
        return datetime.strptime(date_str, format)

    @staticmethod
    def date_to_iso_string(date: datetime) -> str:
        return date.isoformat()

    @staticmethod
    def date_to_string(date: datetime, format: str = default_format) -> str:
        return date.strftime(format)

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
    def is_valid_date_string(date_string: str, format: str = default_format) -> bool:
        try:
            date.fromisoformat(date_string)
            return True
        except ValueError:
            return False