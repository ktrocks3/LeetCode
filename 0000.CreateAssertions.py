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


name = "maxCount"
formatLC("""Example 1:

Input: banned = [1,6,5], n = 5, maxSum = 6
Output: 2
Explanation: You can choose the integers 2 and 4.
2 and 4 are from the range [1, 5], both did not appear in banned, and their sum is 6, which did not exceed maxSum.
Example 2:

Input: banned = [1,2,3,4,5,6,7], n = 8, maxSum = 1
Output: 0
Explanation: You cannot choose any integer while following the mentioned conditions.
Example 3:

Input: banned = [11], n = 7, maxSum = 50
Output: 7
Explanation: You can choose the integers 1, 2, 3, 4, 5, 6, and 7.
They are from the range [1, 7], all did not appear in banned, and their sum is 28, which did not exceed maxSum.""")
testcases("""""[1]
10000
1000000000
[12,12]
13
2199
[8108,8155]
2431
7821
[190,123,20,139,22,140,62,58,137,68,148,172,76,173,189,151,186,153,57,142,105,176,36,104,125,188,152,101,47,51,65,39,174,29,55,13,138,79,81,175,178,42,108,24,80,183,133,114,165,118,56,59,124,82,49,94,8,146,109,14,85,44,60,181,95,23,150,97,28,182,157,46,160,155,12,67,135,117,2,25,74,91,71,98,127,120,130,107,168,18,69,110,61,147,145,38]
3016
240
[264,194,332,88,37,152,38,333,174,237,338,77,308,137,158,197,167,295,319,74,224,78,121,219,281,165,277,227,257,66,148,125,254,129,258,98,191,4,63,172,253,40,221,45,54,132,122,111,110,279,190,299,193,139,41,305,208,105,162,7,19,31,181,252,207,217,133,155,231,84,213,294,97,107,186,101,118,195,315,234,102,182,335,65,248,336,320,34,61,225,112,304,267,59,176,103,270,317,86,340,291,178,204,62,273,99,55,220,256,127,3,296,26,285,242,303,124,230,48,128,8,68,341,255,51,288,334,313,10,32,75,113,14,23,76,157,166,67,306,80,206,246,276,321,145,9,202,222,261,138,73,240,278,282,280,15,71,286,287,90,226,236,330,28,12,96,177,123,115,85,233]
3600
117
[72,244,113,159,330,154,156,311,170,283,9,224,46,197,2,325,237,54,168,275,166,236,179,266,77,196,59,313,286,41,21,201,57,237,74,333,101,281,227,25,138,10,304,55,50,30,250,48,274,331,240,153,312,63,303,342,79,37,165,20,79,293,103,152,215,44,56,196,29,251,264,210,212,135,296,123,289,257,208,309,67,114,170,119,337,163,242,162,109,318,51,105,272,240,107,226,224,188,224,317,27,102,63,128,3,133,27,134,186,220,198,24,274,287,267,8,13,322,278,166,304,165,342,89,184,300,312,339,163,307,123,137,293,227,229,57,66,13,71,233,260,79,228,301,4,4,89,196,193,337,205,51,144,99,104,73,10,311,240,168,77,244,114,217,186,134,229,241,46,89,54,127]
4086
109718563
[193,363,335,233,215,519,180,167,10,501,591,471,421,425,344,533,555,477,59,28,92,66,266,530,595,264,331,462,268,521,401,9,464,275,166,527,218,219,107,34,367,117,42,172,291,392,35,160,294,192,342,168,349,328,578,240,470,301,574,222,173,438,318,476,546,64,542,339,137,585,39,5,312,103,87,372,589,513,217,90,379,161,506,487,326,139,452,525,223,232,429,31,245,198,76,423,255,243,141,303,150,273,529,176,231,73,337,165,494,400,136,142,33,495,369,430,511,498,465,582,199,409,347,537,602,395,83,209,346,548,485,109,333,382,30,248,146,63,315,415,325,327,186,490,133,262,187,360,155,356,532,17,127,13,512,37,386,220,422,457,202,545,373,178,442,428,552,417,113,522,310,330,491,140,260,147,292,507,441,517,3,132,324,469,188,7,461,299,376,115,284,68,480,229,19,162,46,444,394,305,189,18,535,154,263,427,288,420,570,404,478,190,607,49,135,381,343,371,560,144,524,283,259,431,196,278,298,112,316,80,405,29,432,354,86,234,411,447,157,58,85,48,27,104,365,120,397,267,433,253,1,562,221,276,489,575,350,368,52,391,170,252,448,272,443,608,210,446,101,314,16,60,455,138,580,541,99,93,295,601,102,515,62,539,111,364,598,70,466,274,75,399,370,44,45,473,378,282,481,216,171,551,323,317]
125
292541445
[229,274,18,200,350,541,367,302,397,305,171,199,412,556,348,477,381,410,541,415,281,166,224,40,272,585,583,417,353,243,167,335,565,494,52,253,178,198,221,99,126,529,433,322,63,252,131,524,148,355,257,23,224,353,426,593,95,262,332,81,431,359,381,245,219,330,150,488,442,36,57,173,432,55,61,589,68,350,540,424,174,593,378,364,286,35,27,446,504,523,179,25,333,231,137,81,176,516,64,440,484,254,54,337,76,233,26,23,8,601,147,591,93,352,211,336,553,32,61,492,132,179,148,434,69,526,57,345,234,334,205,286,586,501,574,196,563,218,253,462,139,138,436,468,508,416,103,103,408,176,278,299,124,60,204,162,529,19,420,163,188,142,163,382,361,58,315,397,268,33,268,589,505,309,559,186,534,253,521,82,38,595,592,533,288,368,510,433,424,185,60,251,509,45,491,271,54,85,295,569,559,385,182,314,62,116,547,472,214,95,538,538,447,266,323,16,372,361,503,556,3,316,439,394,306,128,163,258,519,228,233,389,518,326,130,152,326,86,87,347,170,155,349,537,300,433,206,214,392,101,401,1,504,473,567,283,412,509,150,388,306,488,327,54,309,255,218,550,584,55,91,430,446,417,279,546,203,281,407,237,443,211,553,225,525,591,431,156,335,203,166,471,208,60,487,358,178,314,290,581,337,224,471,38,176]
7363
911846577 """,
          3)
