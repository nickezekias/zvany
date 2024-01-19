from abc import ABC as Abstract
from dataclasses import asdict, dataclass
from datetime import datetime
import uuid

from src.domain.util.validator import Validator

@dataclass
class Entity(Abstract):
    """Base class for domain models"""
    # FIXME: use a factory to initialize uuid instead of entity abstract class
    # FIX: implement a factory pattern
    # FIX: remove the need for an id in the whole system
    # FIX: or use db generated id and refresh models after transaction commit
    id: str
    errors: list[dict]

    def __init__(self) -> None:

        self.id = ""
        self.errors = []

        if not self.id:
            self.id = uuid.uuid4().hex

    def validate(self) -> None:
        """Check if class' errors list is not empty then raise an error"""
        if len(self.errors) > 0:
            raise ValueError(self.errors)

    def as_dict(self) -> dict:
        """Dump model as dict with dataclass asdict(self) method"""
        return asdict(self)

    def get_class_name(self) -> str:
        """Return the name of the subclass calling this method"""
        return str(type(self))

    def validate_is_datetime(self, attr_name: str, attr_value: datetime) -> bool:
        """
        Checks if attr is nullable datetime and returns True if valid and False if not
            Parameters:
                attr_name (str): A string representing the name of the var
                attr_value (datetime | None): The actual variable representing it's value
                nullable (bool): Can the attribute be None

            Returns:
                is_valid (bool): Validation status, if valid returns True, if not False
        """
        if Validator.is_valid_datetime(attr_value):
            return True
        else:
            self.errors.append(
                {
                    "type": "datetime",
                    "loc": f"{self.get_class_name()}, {attr_name}",
                    "msg": "attribute should be a valid datetime",
                    "input": attr_value,
                }
            )
            return False

    def validate_is_datetime_gte_min(self, attr_name: str, attr_value: datetime, min_value: datetime):
        if Validator.is_datetime_gte_min(attr_value, min_value):
            return True
        else:
            self.errors.append(
                {
                    "type": "datetime",
                    "loc": f"{self.get_class_name()}, {attr_name}",
                    "msg": "attribute should be a valid datetime gte than min_value: ${min_value}",
                    "input": attr_value,
                }
            )
            return False


    def validate_nullable_datetime(
        self, attr_name: str, attr_value: datetime | None
    ) -> bool:
        """
        Checks if attr is nullable datetime and returns True if valid and False if not
            Parameters:
                attr_name (str): A string representing the name of the var
                attr_value (datetime | None): The actual variable representing it's value
                nullable (bool): Can the attribute be None

            Returns:
                is_valid (bool): Validation status, if valid returns True, if not False
        """
        if attr_value is None:
            return True
        elif Validator.is_valid_datetime(attr_value):
            return True
        else:
            self.errors.append(
                {
                    "type": "datetime",
                    "loc": f"{self.get_class_name()}, {attr_name}",
                    "msg": "attribute should be a valid datetime",
                    "input": attr_value,
                }
            )
            return False

    def validate_is_non_empty_string(self, attr_name: str, attr_value: str) -> bool:
        """
        Checks if attr is non-empty string and returns True if valid and False if not
            Parameters:
                attr_name (str): A string representing the name of the var
                attr_value (str): The actual variable representing it's value

            Returns:
                is_valid (bool): Validation status, if valid returns True, if not False
        """
        if Validator.is_non_empty_string(attr_value):
            return True
        else:
            self.errors.append(
                {
                    "type": "str",
                    "loc": f"{self.get_class_name()}, {attr_name}",
                    "msg": "Attribute must be a non-empty str",
                    "input": attr_value,
                }
            )
            return False

    def validate_is_string_with_len_gte_min(self, attr_name: str, attr_value: str, min_str_length: int) -> bool:
        """
        Checks if attr is string with length greater than or equal to min and returns True if valid and False if not
            Parameters:
                attr_name (str): A string representing the name of the var
                attr_value (str): The actual variable representing it's value

            Returns:
                is_valid (bool): Validation status, if valid returns True, if not False
        """
        if Validator.is_string_with_len_gte_min(attr_value, min_str_length):
            return True
        else:
            self.errors.append(
                {
                    "type": "str",
                    "loc": f"{self.get_class_name()}, {attr_name}",
                    "msg": "Attribute must be a string with a length gte {min_str_length}",
                    "input": attr_value,
                }
            )
            return False

    def validate_is_non_empty_set(self, attr_name: str, attr_value: set) -> bool:
        """
        Checks if attr is non-empty python set and returns True if valid and False if not
            Parameters:
                attr_name (str): A string representing the name of the var
                attr_value (set): The actual variable representing it's value

            Returns:
                is_valid (bool): Validation status, if valid returns True, if not False
        """
        if Validator.is_python_set(attr_value) and len(attr_value) >= 1:
            return True
        else:
            self.errors.append(
                {
                    "type": "str",
                    "loc": f"{self.get_class_name()}, {attr_name}",
                    "msg": "Attribute must be a non-empty set",
                    "input": attr_value,
                }
            )
            return False

    # @abstractmethod
    def lazy_validation(self) -> None:
        pass

    def clear_validations(self):
        self.errors = []
