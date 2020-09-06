from .constants import ROMAN_ALGARISMS_VALUE


def main(roman_number: str) -> int:
    decimal_number = 0

    current_biggest_algarism = 1
    for roman_algarism in reversed(roman_number):
        if current_biggest_algarism < ROMAN_ALGARISMS_VALUE[roman_algarism]:
            decimal_number += ROMAN_ALGARISMS_VALUE[roman_algarism]
            current_biggest_algarism = ROMAN_ALGARISMS_VALUE[roman_algarism]

        elif current_biggest_algarism > ROMAN_ALGARISMS_VALUE[roman_algarism]:
            decimal_number -= ROMAN_ALGARISMS_VALUE[roman_algarism]

        else:
            decimal_number += ROMAN_ALGARISMS_VALUE[roman_algarism]

    return decimal_number