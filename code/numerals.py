from .constants import DECIMAL_ROMAN


class Numerals:
    def convert_roman_to_decimal(self, roman: str) -> int:
        decimal = 0
        current_biggest_algarism = 1

        for roman_algarism in reversed(roman):
            decimal_value = DECIMAL_ROMAN[roman_algarism]
            smaller_than_biggest_value = current_biggest_algarism > decimal_value
            update_biggest_value = current_biggest_algarism < decimal_value

            if smaller_than_biggest_value:
                decimal -= decimal_value
            else:
                decimal += decimal_value

            if update_biggest_value:
                current_biggest_algarism = decimal_value

        return decimal
