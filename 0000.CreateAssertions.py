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
    in_out = in_out.split('\n')
    for i in range(len(in_out)):
        if in_out[i].startswith('Input:'):
            input_string, out = in_out[i], in_out[i+1]
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


name = "isArraySpecial"
formatLC("""Example 1:

Input: nums = [3,4,1,2,6], queries = [[0,4]]

Output: [false]

Explanation:

The subarray is [3,4,1,2,6]. 2 and 6 are both even.

Example 2:

Input: nums = [4,3,1,6], queries = [[0,2],[2,3]]

Output: [false,true]""")
testcases("""[586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586]
[586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823,586,1823]
""",
          2)
