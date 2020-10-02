from code.numerals import Numerals

import pytest


@pytest.mark.parametrize(
    "roman_number, decimal_number", [("I", 1), ("II", 2), ("III", 3)]
)
def test_converting_I_II_III_to_1_2_3(roman_number, decimal_number):
    numerals = Numerals()
    result = numerals.convert_roman_to_decimal(roman_number)

    assert result == decimal_number


@pytest.mark.parametrize(
    "roman_number, decimal_number",
    [("IV", 4), ("V", 5), ("VI", 6), ("VII", 7), ("VIII", 8)],
)
def test_converting_IV_V_VI_VII_VIII_to_4_5_6_7_8(roman_number, decimal_number):
    numerals = Numerals()
    result = numerals.convert_roman_to_decimal(roman_number)

    assert result == decimal_number


@pytest.mark.parametrize(
    "roman_number, decimal_number",
    [("IX", 9), ("X", 10), ("XI", 11), ("XII", 12), ("XIII", 13)],
)
def test_converting_IX_X_XI_XII_XIII_to_9_10_11_12_13(roman_number, decimal_number):
    numerals = Numerals()
    result = numerals.convert_roman_to_decimal(roman_number)

    assert result == decimal_number
