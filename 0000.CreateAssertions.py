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


name = "maxSumOfThreeSubarrays"
func = ""
func2 = ""
formatLC("""Example 1:

Input: words = ["acca","bbbb","caca"], target = "aba"
Output: 6
Explanation: There are 6 ways to form target.
"aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("caca")
"aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("caca")
"aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("acca")
"aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("acca")
"aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("acca")
"aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("caca")
Example 2:

Input: words = ["abba","baab"], target = "bab"
Output: 4
Explanation: There are 4 ways to form target.
"bab" -> index 0 ("baab"), index 1 ("baab"), index 2 ("abba")
"bab" -> index 0 ("baab"), index 1 ("baab"), index 3 ("baab")
"bab" -> index 0 ("baab"), index 2 ("baab"), index 3 ("baab")
"bab" -> index 1 ("abba"), index 2 ("baab"), index 3 ("baab")
 
 
 """)
# testcases(""" """", 0)
