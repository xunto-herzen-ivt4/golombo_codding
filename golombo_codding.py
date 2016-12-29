from base_numeral_system import base_ns
from haffman_codding import haffman_codding
from unary_codding import unary
import math


def haffman_for_mods(m):
    mods = ""

    # Haffman_codding only works with strings
    # so we put everything in string
    for i in range(0, m):
        mod = str(i)
        if mod not in mods:
            mods += mod

    codes, _ = haffman_codding.encode(mods)

    # Convert code's keys to numbers
    result = {}
    for key in codes.keys():
        new_key = int(key)
        result[new_key] = codes[key]

    return result


def is_power_of_two(m):
    i = 0

    binary = base_ns.convert(m, 2).integer
    for digit in binary:
        if digit == 1:
            i += 1

    return i == 1


def add_zeros_in_begining(code: list, size: int):
    return ([0] * (size - len(code))) + code


def encode(data: list, m):
    # Encode phrase
    result = []

    power_of_two = is_power_of_two(m)
    codes = haffman_for_mods(m)

    for number in data:
        div, mod = divmod(number, m)
        code = unary.encode([div])
        if power_of_two:
            tmp = int(math.ceil(math.log(m, 2)))
            code += add_zeros_in_begining(base_ns.convert(mod, 2).integer[:tmp], tmp)
        else:
            code += codes[mod]
        result += code

    return result


def find_first_code(data: list, codes: dict):
    for key, code in codes.items():
        if data[:len(code)] == code:
            return key
    return None


def decode(encoded_data: list, m):
    encoded_data = encoded_data[:]
    result = []

    power_of_two = is_power_of_two(m)
    codes = haffman_for_mods(m)

    integer = 0
    while len(encoded_data) > 0:
        item = encoded_data.pop(0)
        if item == 0:
            if power_of_two:
                size = int(math.ceil(math.log(m, 2)))
                mod = int(base_ns.convert_to_dec(base_ns.NumberBased(2, encoded_data[:size])))
            else:
                mod = find_first_code(encoded_data, codes)
                size = len(codes[mod])

            encoded_data = encoded_data[size:]
            result.append(m * integer + mod)
            integer = 0
        else:
            integer += 1

    return result
