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


name = "checkIfExist"
formatLC("""Input: arr = [10,2,5,3]
Output: true""")
formatLC("""Input: arr = [3,1,7,11]
Output: false""")
testcases("""[0,0]
[-2,0,10,-19,4,6,-8]
[-16,-13,8]
[10,2,7,3,0,0,-13]
[7,15,3,4,30]
[0,2,-7,11,4,18]
[357,-53,277,-706,980,826,93,-352,-669,989,-193,920,209,-574,-389,221,383,352,665,873,759,-480,-64,-103,-721,-623,-642,-680,20,-168,528,-336,-656,264,581,-714,-458,721,815,106,328,476,351,325,-954,890,-174,635,95,-443,338,907,-648,113,-278,498,532,-778,95,-487,-909,-642,774,296,417,-132,-951,857,-867,321,-960,180,108,-984,-54,103,703,-118,-252,235,577,-703,842,-638,-888,-981,-246,484,202,328,661,447,-831,946,-888,-749,-702]
[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997]""",
          1)
