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


name = "minRemoval"
func = ""
func2 = ""
formatLC("""


Example 1:

Input: nums = [2,1,5], k = 2

Output: 1

Explanation:

Remove nums[2] = 5 to get nums = [2, 1].
Now max = 2, min = 1 and max <= min * k as 2 <= 1 * 2. Thus, the answer is 1.
Example 2:

Input: nums = [1,6,2,9], k = 3

Output: 2

Explanation:

Remove nums[0] = 1 and nums[3] = 9 to get nums = [6, 2].
Now max = 6, min = 2 and max <= min * k as 6 <= 2 * 3. Thus, the answer is 2.
Example 3:

Input: nums = [4,6], k = 2

Output: 0

Explanation:

Since nums is already balanced as 6 <= 4 * 2, no elements need to be removed.
 """)
testcases("""[2,1,5]
2
[2,12]
2
[8]
1
[32,607,740,134,944,91,410,155,493,89,12]
10
[1,34,23]
2
[26155,1776,22815,775,27772,12869,12995,22794,27692,24728,10944,25039,24068,25506,18506,19138,12331,17814,20834,21474,20208,21590,15453,6114,25716,29434,23547,29051,25992,5535,7387]
80020
[9514,4037,4183,20670,24972,13008,31534,34223,22722,7793,15527,37410,28870,7506,3485,19748,26934,333,38955,831,6658,24063,10075,14595,15246,5715,3382,27295,6093,24611,14191,31204,14631,12630]
1""", 2)
