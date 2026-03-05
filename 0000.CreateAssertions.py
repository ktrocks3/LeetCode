def makeAssertion(args: str, sol: str):
    global name
    params = args[1:len(args) - 1]
    fn = f'Solution().{name}'
    if func == "":
        print(f'assert {fn}({params}) == {sol}, \\ \n  f\'Expected: {sol}, Received: {{{fn}({params})}}\'')
    elif func2 == "":
        problem = f'{fn}({func}({params}))'
        print(f'assert {problem} == {sol}, \\'
              f'\n  f\'Expected: {sol}, Received: {{{problem}}}\'')
    else:
        problem = f'{fn}({func}({params}))'
        sol = f'{func2}({sol})'
        print(f'assert {problem} == {sol}, \\'
              f'\n  f\'Expected: {sol}, Received: {{ {problem} }}\' ')


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


name = "minOperations"
func = ""
func2 = ""
formatLC("""

You are given a string s consisting only of the characters '0' and '1'. In one operation, you can change any '0' to '1' or vice versa.

The string is called alternating if no two adjacent characters are equal. For example, the string "010" is alternating, while the string "0100" is not.

Return the minimum number of operations needed to make s alternating.

 

Example 1:

Input: s = "0100"
Output: 1
Explanation: If you change the last character to '1', s will be "0101", which is alternating.
Example 2:

Input: s = "10"
Output: 0
Explanation: s is already alternating.
Example 3:

Input: s = "1111"
Output: 2
Explanation: You need two operations to reach "0101" or "1010".
 
 
 """)
# testcases(""" """, 2)
