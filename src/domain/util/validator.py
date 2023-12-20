from datetime import datetime
from src.domain.util.date_time_util import DateTimeUtil

class Validator:

    @staticmethod
    def is_valid_datetime(value: datetime) -> bool:
        """Check value is valid datetime"""
        if value and DateTimeUtil.is_valid_date(value):
            return True
        return False

    @staticmethod
    def is_datetime_gt_min(value: datetime, min_value: datetime) -> bool:
        """Check is datetime with the right min"""
        if Validator.is_valid_datetime(value) and value > min_value:
            return True
        return False

    @staticmethod
    def is_string(value: str) -> bool:
        """Check value is str"""
        if isinstance(value, str):
            return True
        return False

    @staticmethod
    def is_non_empty_string(value: str) -> bool:
        """Simply checks value is non empty string"""
        if Validator.is_string(value) and value != "":
            return True
        return False

    @staticmethod    
    def is_string_with_len_gte_min(value: str, min_value: int) -> bool:
        """Check value is str greater than or equal to min"""
        if Validator.is_string(value) and len(value) >= min_value:
            return True
        return False

    @staticmethod
    def is_int(value: int) -> bool:
        """Simply checks if value is int"""
        if isinstance(value, int):
            return True
        return False

    @staticmethod
    def is_int_gte_min(value: int, min_value: int) -> bool:
        """Checks if val is int greater than or equal to min"""
        if Validator.is_int(value) and value >= min_value:
            return True
        return False

    @staticmethod
    def is_int_lte_max(value: int, max_value: int) -> bool:
        """Checks if val is int lesser than or equal to max"""
        if Validator.is_int(value) and value <= max_value:
            return True
        return False

    @staticmethod
    def is_int_between_min_max(value: int, min_value: int,  max_value: int) -> bool:
        """Checks if int has the right min and max"""
        if Validator.is_int_gte_min(value, min_value) and Validator.is_int_lte_max(value, max_value):
            return True
        return False

    @staticmethod
    def is_python_set(value: set) -> bool:
        if not isinstance(value, set):
            return False
        return True