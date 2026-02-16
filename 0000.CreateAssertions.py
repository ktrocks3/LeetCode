def makeAssertion(args: str, sol: str):
    global name
    if func == "":
        print(f'assert Solution().{name}({args[1:len(args) - 1]}) == {sol}, \\'
              f'\n  f\'Expected: {sol}, Received: {{Solution().{name}({args[1:len(args) - 1]})}}\'')
    elif func2 == "":
        print(f'assert Solution().{name}({func}({args[1:len(args) - 1]})) == {sol}, \\'
              f'\n  f\'Expected: {sol}, Received: {{Solution().{name}({func}({args[1:len(args) - 1]}))}}\'')
    else:
        print(f'assert {func2}(Solution().{name}({func}({args[1:len(args) - 1]}))) == {sol}, \\'
              f'\n  f\'Expected: {sol}, Received: {func2}({{Solution().{name}({func}({args[1:len(args) - 1]}))}})\'')


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
    return [eval(value.replace('null', 'None')) for value in values]


def formatLC(in_out: str):
    in_out = in_out.split('\n')
    while '' in in_out: in_out.remove('')
    for i in range(len(in_out)):
        if in_out[i].startswith('Input:'):
            input_string, out = in_out[i], in_out[i + 1]
            i += 1
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


name = "reverseBits"
func = ""
func2 = ""
formatLC("""
 Example 1:

Input: n = 43261596

Output: 964176192

Explanation:

Integer	Binary
43261596	00000010100101000001111010011100
964176192	00111001011110000010100101000000
Example 2:

Input: n = 2147483644

Output: 1073741822

Explanation:

Integer	Binary
2147483644	01111111111111111111111111111100
1073741822	00111111111111111111111111111110

 
 """)
# testcases(""" """, 2)
