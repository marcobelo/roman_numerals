from .constants import ROMAN_ALGARISMS_VALUE


def main(roman_number: str) -> int:
    decimal_number = 0

    for roman_algarism in reversed(roman_number):
        decimal_number += ROMAN_ALGARISMS_VALUE[roman_algarism]

    return decimal_number