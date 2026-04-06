from typing import List


class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        class Robot:
            def __init__(self, position, health, direction):
                self.position = position
                self.health = health
                self.direction = direction
                self.alive = True

            def __str__(self):
                return f"Robot({self.position}, {self.health}, {self.direction})" if self.alive else "Dead"

            def __repr__(self):
                return self.__str__()

        def collide(r1: Robot, r2: Robot) -> Robot | None:
            # assumes r1 is 'R' and r2 is 'L'
            if r1.health == r2.health:
                r1.alive = False
                r2.alive = False
                return None
            elif r1.health < r2.health:
                r1.alive = False
                r2.health -= 1
                return r2
            else:
                r2.alive = False
                r1.health -= 1
                return r1

        # First I'll convert into robot type
        robots = []
        for i in range(len(positions)):
            robots.append(Robot(positions[i], healths[i], directions[i]))
        sorted_robots = sorted(robots, key=lambda x: x.position)
        stack = []

        for robot in sorted_robots:
            # Only collide while top is R and current is L
            while stack and stack[-1].direction == 'R' and robot.direction == 'L':
                survivor = collide(stack.pop(), robot)
                if survivor is None:
                    robot = None
                    break
                elif survivor.direction == 'R':
                    stack.append(survivor)
                    robot = None
                    break
                else:
                    robot = survivor

            if robot is not None:
                stack.append(robot)

        return [r.health for r in robots if r.alive]


assert Solution().survivedRobotsHealths([5, 4, 3, 2, 1], [2, 17, 9, 15, 10], 'RRRRR') == [2, 17, 9, 15, 10], \
    f'Expected: [2,17,9,15,10], Received: {Solution().survivedRobotsHealths([5, 4, 3, 2, 1], [2, 17, 9, 15, 10], 'RRRRR')}'
assert Solution().survivedRobotsHealths([3, 5, 2, 6], [10, 10, 15, 12], 'RLRL') == [14], \
    f'Expected: [14], Received: {Solution().survivedRobotsHealths([3, 5, 2, 6], [10, 10, 15, 12], 'RLRL')}'
assert Solution().survivedRobotsHealths([1, 2, 5, 6], [10, 10, 11, 11], 'RLRL') == [], \
    f'Expected: [], Received: {Solution().survivedRobotsHealths([1, 2, 5, 6], [10, 10, 11, 11], 'RLRL')}'
assert Solution().survivedRobotsHealths([3, 47], [46, 26], 'LR') == [46, 26], \
    f'Expected: [], Received: {Solution().survivedRobotsHealths([3, 47], [46, 26], 'LR')}'
