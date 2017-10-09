from bmi_complete import calculate_bmi
import pytest


def test_calculate_bmi_normal_values():
    result = calculate_bmi(70, 1.8)
    assert result == 21.604938271604937


def test_exception():
    with pytest.raises(ZeroDivisionError) as excinfo:
        calculate_bmi(70, 0)
    assert str(excinfo.value) == "division by zero"
