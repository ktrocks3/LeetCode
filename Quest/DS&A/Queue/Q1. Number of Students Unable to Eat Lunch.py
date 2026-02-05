from typing import List
from collections import deque


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        sandwiches = deque(sandwiches)

        while sandwiches:
            sandwich = sandwiches[0]
            attempts = len(students)

            while attempts > 0 and students[0] != sandwich:
                students.append(students.popleft())
                attempts -= 1

            if attempts == 0:
                return len(students)

            sandwiches.popleft()
            students.popleft()

        return len(students)


assert Solution().countStudents([1, 1, 0, 0], [0, 1, 0, 1]) == 0, \
    f'Expected: 0, Received: {Solution().countStudents([1, 1, 0, 0], [0, 1, 0, 1])}'
assert Solution().countStudents([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1]) == 3, \
    f'Expected: 3, Received: {Solution().countStudents([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1])}'
