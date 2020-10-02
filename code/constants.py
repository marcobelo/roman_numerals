def _add_dict_reverse(dictionary):
    dictionary.update({value: key for key, value in dictionary.items()})


DECIMAL_ROMAN = {"I": 1, "V": 5, "X": 10}
_add_dict_reverse(DECIMAL_ROMAN)