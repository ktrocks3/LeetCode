from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in ['+', '-', '*', '/']:
                y, x = stack.pop(), stack.pop()
                match t:
                    case '+':
                        stack.append(x + y)
                    case '-':
                        stack.append(x - y)
                    case '*':
                        stack.append(x * y)
                    case '/':
                        stack.append(int(x / y))
            else:
                stack.append(int(t))
        return stack.pop()


assert Solution().evalRPN(['2', '1', '+', '3', '*']) == 9, \
    f'Expected: 9, Received: {Solution().evalRPN(['2', '1', '+', '3', '*'])}'
assert Solution().evalRPN(['4', '13', '5', '/', '+']) == 6, \
    f'Expected: 6, Received: {Solution().evalRPN(['4', '13', '5', '/', '+'])}'
assert Solution().evalRPN(['10', '6', '9', '3', '+', '-11', '*', '/', '*', '17', '+', '5', '+']) == 22, \
    f'Expected: 22, Received: {Solution().evalRPN(['10', '6', '9', '3', '+', '-11', '*', '/', '*', '17', '+', '5', '+'])}'
