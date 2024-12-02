from typing import List
import re


def makeAssertion(args: str, sol: str):
    global name
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


def formatLC(in_out: str):
    input_string, out = in_out.split('\n')
    out = out[7:].strip()
    if out == "true":
        out = "True"
    if out == "false":
        out = "False"
    parsed_values = str(parse_input(input_string))
    makeAssertion(parsed_values, out)


def testcases(case: str, num: int):
    case = case.split('\n')
    for i in range(0, len(case), num):
        collected = []
        for j in range(num):
            collected.append(case[i + j])
        collected = ','.join(collected)
        print(f'Solution().{name}({collected})')


name = "isPrefixOfWord"
formatLC("""Input: sentence = "i love eating burger", searchWord = "burg"
Output: 4""")
formatLC("""Input: sentence = "this problem is an easy problem", searchWord = "pro"
Output: 2""")
formatLC("""Input: sentence = "i am tired", searchWord = "you"
Output: -1""")
testcases(""""i love eating bunburger burger"
"burg"
"hellohello hellohellohello"
"ello"
"i love eating broadburgers"
"burg"
"love i love eating bunburger burger"
"i"
"helloh hellohe"
"hellohe"
"winstontang love they i pillow jonathan you winstontang pillow dream you duck"
"p"
"love"
"lov"
"hello from the other side"
"they" """,
          2)
