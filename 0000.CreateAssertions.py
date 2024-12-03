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


name = "addSpaces"
formatLC("""Input: s = "LeetcodeHelpsMeLearn", spaces = [8,13,15]
Output: "Leetcode Helps Me Learn" """)
formatLC("""Input: s = "icodeinpython", spaces = [1,5,7,9]
Output: "i code in py thon" """)
formatLC("""Input: s = "spacing", spaces = [0,1,2,3,4,5,6]
Output: " s p a c i n g" """)
testcases(""""LeetcodeHelpsMeLearn"
[8,13,15]
"icodeincpp"
[1,5,7,9]
"spacing"
[0,1,2,3,4,5,6]
"AllEyesOnHindu"
[7]
"MakeIndiaGreatAgain"
[1,7,8,9]
"DelhiMeiBJP"
[8,9]
"HinduMeansIndian"
[9,11]
"jaimatadi"
[7,8] """,
          2)
