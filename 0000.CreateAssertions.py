from typing import List
import re


def makeAssertion(name: str, args: str, sol: str):
    print(f'assert Solution().{name}({args[1:len(args) - 1]}) == {sol}, \\'
          f'\n  f\'Expected: {sol}, Received: {{Solution().{name}({args[1:len(args) - 1]})}}\'')


def parse_input(input_string):
    values = []
    buffer = ""
    depth = 0

    for char in input_string:
        if char == "," and depth == 0:  # Split only at top-level commas
            if "=" in buffer:
                values.append(buffer.split("=", 1)[1].strip())
            buffer = ""
        else:
            if char == "[":
                depth += 1
            elif char == "]":
                depth -= 1
            buffer += char

    # Add the last captured value
    if buffer and "=" in buffer:
        values.append(buffer.split("=", 1)[1].strip())

    # Evaluate the captured values to convert strings to lists, ints, etc.
    return [eval(value) for value in values]


def formatLC(in_out: str, name: str):
    input_string, out = in_out.split('\n')
    out = out[7:].strip()
    if out == "true":
        out = "True"
    if out == "false":
        out = "False"
    parsed_values = str(parse_input(input_string))
    makeAssertion(name, parsed_values, out)


formatLC("""Input: stones = [0,1,3,5,6,8,12,17]
Output: true""", 'canCross')
formatLC("""Input: stones = [0,1,2,5,6,9,10,12,13,14,17,19,20,21,26,27,28,29,30]
Output: false""", 'canCross')
