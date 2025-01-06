from datetime import date
import pytest
from seasons import Birth


def test_valid_date_past():
    birth = Birth.get("1999-01-01")
    assert isinstance(birth, Birth)
    assert birth.year == 1999
    assert birth.month == 1
    assert birth.day == 1

def test_invalid_date_format():
    with pytest.raises(SystemExit) as e:
        Birth.get("01-01-2000")
    assert str(e.value) == "Invalid date"

def test_invalid_date_logical():
    with pytest.raises(SystemExit) as e:
        Birth.get("2025-12-32")
    assert str(e.value) == "Invalid date"

def test_future_date():
    with pytest.raises(SystemExit) as e:
        Birth.get("2030-01-01")
    assert str(e.value) == "Invalid date"

def test_output_format():
    birth = Birth.get("2000-01-01")
    assert str(birth).startswith("Thirteen million")
