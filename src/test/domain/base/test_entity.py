from datetime import datetime
from src.domain.base.entity import Entity

now = datetime.now()
entity = Entity()

def test_validate_is_datetime():
    res = entity.validate_is_datetime("now", now)
    assert res is True

def test_validate_is_datetime_err_payload_not_type_datetime():
    res = entity.validate_is_datetime("now", "now") #type: ignore - testing bad type
    assert res is False

def test_validate_nullable_datetime():
    res = entity.validate_nullable_datetime("now", now)
    assert res is True

def test_validate_nullable_datetime_payload_is_none():
    res = entity.validate_nullable_datetime("now", None)
    assert res is True

def test_validate_nullable_datetime_err_payload_is_not_type_datetime():
    res = entity.validate_nullable_datetime("now", "2023-05-05T01:00:00") # type: ignore - testing bad payload type
    assert res is False

def test_validate_is_non_empty_string():
    res = entity.validate_is_non_empty_string("text", "Hello World")
    assert res is True

def test_validate_is_non_empty_string_err_payload_not_type_str():
    res = entity.validate_is_non_empty_string("text", 83923) # type: ignore - testing bad payload type
    assert res is False

def test_validate_is_non_empty_string_err_payload_is_none():
    res = entity.validate_is_non_empty_string("text", "") # type: ignore - testing bad payload type
    assert res is False

def test_validate_is_string_with_len_gte_min():
    res = entity.validate_is_string_with_len_gte_min("text", "Hello World", 11)
    assert res is True

def test_validate_is_string_with_len_gte_min_err_payload_strlen_inf_min():
    res = entity.validate_is_string_with_len_gte_min("text", "Hello World", 12)
    assert res is False

def test_validate_is_non_empty_set():
    res = entity.validate_is_non_empty_set("set", {38, "Hello World"})
    assert res is True

def test_validate_is_non_empty_set_err_payload_is_empty():
    res = entity.validate_is_non_empty_set("set", {}) # type: ignore - testing empty set
    assert res is False

def test_validate_is_non_empty_set_err_payload_type_is_not_set():
    res = entity.validate_is_non_empty_set("set", {"greetings": "Hello World"}) # type: ignore - testing bad type
    assert res is False
