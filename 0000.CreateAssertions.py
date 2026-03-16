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


name = "getBiggestThree"
func = ""
func2 = ""
formatLC("""
You are given an m x n integer matrix grid​​​.

A rhombus sum is the sum of the elements that form the border of a regular rhombus shape in grid​​​. The rhombus must have the shape of a square rotated 45 degrees with each of the corners centered in a grid cell. Below is an image of four valid rhombus shapes with the corresponding colored cells that should be included in each rhombus sum:


Note that the rhombus can have an area of 0, which is depicted by the purple rhombus in the bottom right corner.

Return the biggest three distinct rhombus sums in the grid in descending order. If there are less than three distinct values, return all of them.

 

Example 1:


Input: grid = [[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]
Output: [228,216,211]
Explanation: The rhombus shapes for the three biggest distinct rhombus sums are depicted above.
- Blue: 20 + 3 + 200 + 5 = 228
- Red: 200 + 2 + 10 + 4 = 216
- Green: 5 + 200 + 4 + 2 = 211
Example 2:


Input: grid = [[1,2,3],[4,5,6],[7,8,9]]
Output: [20,9,8]
Explanation: The rhombus shapes for the three biggest distinct rhombus sums are depicted above.
- Blue: 4 + 2 + 6 + 8 = 20
- Red: 9 (area 0 rhombus in the bottom right corner)
- Green: 8 (area 0 rhombus in the bottom middle)
Example 3:

Input: grid = [[7,7,7]]
Output: [7]
Explanation: All three possible rhombus sums are the same, so return [7].
 
 
 
 """)
# testcases(""" """, 2)
