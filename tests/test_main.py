from code.__init__ import main

import pytest


@pytest.mark.parametrize(
    "roman_number, decimal_number", [("I", 1), ("II", 2), ("III", 3)]
)
def test_main_converting_I_II_III_to_1_2_3(roman_number, decimal_number):
    result = main(roman_number)

    assert result == decimal_number


@pytest.mark.parametrize(
    "roman_number, decimal_number",
    [("IV", 4), ("V", 5), ("VI", 6), ("VII", 7), ("VIII", 8)],
)
def test_main_converting_IV_V_VI_VII_VIII_to_4_5_6_7_8(roman_number, decimal_number):
    result = main(roman_number)

    assert result == decimal_number
