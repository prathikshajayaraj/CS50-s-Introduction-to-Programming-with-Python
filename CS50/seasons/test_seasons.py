from datetime import date
import pytest
from seasons import Minutes

def test_init_valid_date():
    try:
        m = Minutes("2023-08-02")
        assert m.user == "2023-08-02"
    except ValueError:
        pytest.fail("Unexpected ValueError for valid date")

def test_init_invalid_date():
    with pytest.raises(ValueError):
        Minutes("2000-13-01")

def test_str():
    m = Minutes("2023-08-02")
    m.today = date(2024, 8, 2)
    m.calculate_difference()
    assert str(m) == "Five hundred twenty-seven thousand forty minutes"

def test_calculate_difference():
    m = Minutes("2023-08-02")
    m.today = date(2024, 8, 2)
    m.calculate_difference()
    expected_minutes = (m.today - m.dateconversion).days * 24 * 60
    assert m.minutes == expected_minutes

def test_word_minutes():
    m = Minutes("2023-08-02")
    minutes = 527040
    words = m.word_minutes(minutes)
    assert words == "Five hundred twenty-seven thousand forty"
