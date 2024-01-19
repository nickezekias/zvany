from datetime import datetime, timedelta

from src.domain.util.validator import Validator

now = datetime.now()

def test_is_valid_datetime():
    res = Validator.is_valid_datetime(now)
    assert res is True

def test_is_valid_datetime_err_payload_wrong_type():
    res = Validator.is_valid_datetime("Help") # type: ignore - testing false positive
    assert res is False

def test_is_datetime_gt_min():
    dt = now + timedelta(milliseconds=1)
    res = Validator.is_datetime_gte_min(dt, now)
    assert res is True

def test_is_datetime_gt_min_err_payload_lt_min():
    dt = now - timedelta(milliseconds=1)
    res = Validator.is_datetime_gte_min(dt, now)
    assert res is False

def test_is_non_empty_string():
    res = Validator.is_non_empty_string("H")
    assert res is True

# this implicitly tests the Validator.is_string() method
def test_is_non_empty_string_err_payload_not_str():
    res = Validator.is_non_empty_string(83092) # type: ignore testing false positive
    assert res is False

def test_is_non_empty_string_err_payload_empty():
    res = Validator.is_non_empty_string("")
    assert res is False

def test_is_string_with_len_gte_min():
    res = Validator.is_string_with_len_gte_min("nick", 3)
    assert res is True

def test_is_string_with_len_gte_min_err_payload_gte_min():
    res = Validator.is_string_with_len_gte_min("nick", 5)
    assert res is False

def test_is_int_gte_min():
    res = Validator.is_int_gte_min(3, 3)
    assert res is True

def test_is_int_gte_min_err_payload_lt_min():
    res = Validator.is_int_gte_min(2, 3)
    assert res is False

def test_is_int_lte_max():
    res = Validator.is_int_lte_max(3, 3)
    assert res is True

def test_is_int_lte_max_err_payload_gt_max():
    res = Validator.is_int_lte_max(4, 3)
    assert res is False


def test_is_int_between_min_max():
    res = Validator.is_int_between_min_max(3, 3, 4)
    assert res is True

def test_is_int_between_min_max_err_payload_lt_min():
    res = Validator.is_int_between_min_max(2, 3, 4)
    assert res is False

def test_is_int_between_min_max_err_payload_gt_max():
    res = Validator.is_int_between_min_max(3, 3, 2)
    assert res is False

def test_is_int_between_min_max_err_payload_lt_min_and_gt_max():
    res = Validator.is_int_between_min_max(2, 3, 1)
    assert res is False
