import pytest

from .part8 import *


def test_raise_exception():
    with pytest.raises(RuntimeError):
        raise_exception()


def test_raise_exception_on_negative():
    with pytest.raises(RuntimeError):
        raise_exception_on_negative(-1)


def test_raise_exception_on_negative_pos():
    raise_exception_on_negative(1)


def test_raise_exception_with_message():
    with pytest.raises(RuntimeError, match=r"rare boel"):
        raise_exception_with_message()


def test_handle_exception_ok():
    r = handle_exception(10, 2)
    assert r == 5


def test_handle_exception():
    r = handle_exception(10, 0)
    assert r is None


def test_custom_exception():
    with pytest.raises(TooLazyError):
        raise_custom_exception()


def test_custom_exception_with_message():
    with pytest.raises(TooTiredError, match=r"te moe"):
        raise_custom_exception_with_message()


def test_bmi_weight_zero():
    with pytest.raises(WeightError):
        calculate_bmi(0, 1.83)


def test_bmi_height_zero():
    with pytest.raises(HeightError):
        calculate_bmi(77, 0)


def test_bmi_height_zero_exception_with_message():
    with pytest.raises(HeightError, match=r"lengte is 0"):
        calculate_bmi(77, 0)
