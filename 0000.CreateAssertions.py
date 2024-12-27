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


name = "maxScoreSightseeingPair"
func = ""
func2 = ""
formatLC("""Example 1:

Input: values = [8,1,5,2,6]
Output: 11
Explanation: i = 0, j = 2, values[i] + values[j] + i - j = 8 + 5 + 0 - 2 = 11
Example 2:

Input: values = [1,2]
Output: 2
 
 """)
testcases("""[5,4,null,8,null,null,1]
[1,3,null,null,4,null,5]
[50,38,30,45,null,1,null,null,31]
[29,13,40,32,null,20,null,null,null,49,21,50,null,null,null,1]
[370,108,365,235,447,301,26,311,259,null,null,null,null,null,21,null,null,null,274,352,null,null,null,401,467]
[78,88,76,null,137,212,397,null,169,311,27,15,140,257,163,253,null,null,161,381,398,null,357,null,25,null,null,null,null,null,328,null,null,null,217,23,104,null,196,null,264,null,null,null,null,301,null,null,null,null,491,59,473,null,null,null,209,249,452,273,64,null,349,86,null,null,null,168,null,337,192,494,null,null,null,222,43]
[789,637,24,321,247,81,171,285,367,null,null,69,478,483,76,46,454,null,437,1863,348,null,466,262,null,205,40,null,441,473,202,246,332,488,183,394,null,411,null,191,null,176,33,203,null,302,null,null,58,53,365,null,343,null,138,null,43,56,null,233,null,null,122,null,null,407,465,null,154,312,420,null,null,null,null,425,93,222,17,101,null,null,112,null,null,259,null,null,null,null,null,353,250,275,null,null,168,null,null,null,null,391,458,277,null,288,null,null,null,268,244,393,339,null,null,482,null,null,481,null,360,null,null,null,null,null,99,null,null,220,null,null,null,null,374,null,399,270,null,null,null,371,null,null,null,null,null,null,null,null,null,177,null,79]""",
          2)
