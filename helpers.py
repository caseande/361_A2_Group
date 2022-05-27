
def num_is_valid(num_str):
    # cannot be empty string
    if not num_str or not isinstance(num_str, str):
        return False
    # cannot have more than 1 decimal
    elif num_str.count(".") > 1:
        return False

    # temporarily deal with negatives
    if num_str[0] == "-":
        num_str = num_str[1:]

    # everything after 0x should be valid
    if num_str[:2] == "0x":
        allowed = "ABCDEF0123456789"
        for letter in num_str[2:]:
            if letter.upper() not in allowed:
                return False
        # if everything after 0x is valid then num_str is valid
        return True
    # there shouldn't be any hex numbers without the 0x leading
    elif "x" in num_str or "X" in num_str:
        return False

    # if it doesn't start with 0x it shouldn't have non numbers after
    for letter in num_str:
        if letter == ".":
            continue
        elif not letter.isnumeric():
            return False

    #  otherwise valid num_str
    return True
