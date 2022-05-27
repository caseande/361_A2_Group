from helpers import num_is_valid


def conv_num(num_str):
    # check if valid number
    if not num_is_valid(num_str):
        return None

    # if negative, remove -1 and turn on negative flag
    negative_flag = False
    if num_str[0] == "-":
        num_str = num_str[1:]
        negative_flag = True

    # if hex
    if num_str[:2] == "0x":
        hex_conversion = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "A": 10,
            "B": 11,
            "C": 12,
            "D": 13,
            "E": 14,
            "F": 15,
        }
        number = 0
        remaining = num_str[2:]
        power = len(remaining) - 1
        for letter in remaining:
            number += hex_conversion[letter.upper()] * (16**power)
            power -= 1

    # if valid float
    elif "." in num_str:
        number = 0.00
        power = 1
        period_flag = False
        for index in num_str:
            if index == ".":
                period_flag = True
            elif period_flag:
                number += (ord(index) - 48) / (10**power)
                power += 1
            else:
                number = number * 10 + (ord(index) - 48)
    else:
        # if valid int
        number = 0
        for index in num_str:
            number = number * 10 + (ord(index) - 48)

    # if negative flag set then x -1
    if negative_flag:
        return number * -1
    else:
        return number


def conv_endian(num, endian='big'):
    """
    converts decimal value to hexadecimal
    """
    if num == 0:
        return "00"
    elif num == "":
        return None
    # default false for neg flag
    is_neg = False
    if num < 0:
        is_neg = True
        num *= -1

    # https://www.geeksforgeeks.org/program-decimal-hexadecimal-conversion/
    hex_arr = ""
    while num != 0:
        temp = num % 16
        # check if temp < 10
        if temp < 10:
            hex_arr += chr(temp + 48)
        else:
            hex_arr += chr(temp + 55)
        num = num // 16

    # reverse result
    # https://stackoverflow.com/questions/931092/reverse-a-string-in-python
    print(hex_arr)
    hex_string = hex_arr[::-1]

    # create output string
    output = ""
    # if string is not even, add 0
    is_even = True
    if len(hex_string) % 2 != 0:
        output += "0"
        is_even = False

    if endian == 'big':
        for i in range(0, len(hex_string)):
            output += hex_string[i]
            if is_even:
                if i % 2 != 0 and i != len(hex_string) - 1:
                    output += " "
            elif not is_even:
                if i % 2 == 0 and i != len(hex_string) - 1:
                    output += " "
        if is_neg:
            output = ''.join(('-', output))
        print(output)
        return output
    elif endian == 'little':
        for i in range(0, len(hex_string)):
            output += hex_string[i]
        # https://stackoverflow.com/questions/5864271/reverse-a-string-in-python-two-characters-at-a-time-network-byte-order
        output = "".join(reversed([output[i:i+2] for i in range(0, len(output), 2)]))
        final = ""
        for i in range(0, len(output)):
            final += output[i]
            if i % 2 != 0 and i != len(output) - 1:
                final += " "
        if is_neg:
            final = ''.join(('-', final))
        print(final)
        return final
    else:
        return None
