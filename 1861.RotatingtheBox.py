from typing import List


class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        # Simulate gravity for each row
        for column in box:
            # Use two-pointer approach to "fall" stones into the available spaces
            empty = len(column) - 1  # Start with the rightmost position
            for i in range(len(column) - 1, -1, -1):  # Traverse from right to left
                if column[i] == "#":  # If it's a stone
                    column[i], column[empty] = ".", "#"  # Swap with the empty space
                    empty -= 1  # Update the empty position
                elif column[i] == "*":  # If it's an obstacle
                    empty = i - 1  # Reset the empty position to just left of the obstacle

        # Rotate the box
        rows, cols = len(box), len(box[0])
        rotated_box = [[box[rows - 1 - j][i] for j in range(rows)] for i in range(cols)]

        return rotated_box


assert Solution().rotateTheBox([["#", ".", "#"]]) == [["."], ["#"], [
    "#"]], f"Expected [[.], [#], [#]], received {Solution().rotateTheBox([["#", ".", "#"]])}"

assert (Solution().rotateTheBox([["#", ".", "*", "."], ["#", "#", "*", "."]]) ==
        [["#", "."], ["#", "#"], ["*", "*"], [".", "."]]), \
    (f"Expected [[#,.], [#,#], [*,*], [.,.]], received "
     f"{Solution().rotateTheBox([["#", ".", "*", "."], ["#", "#", "*", "."]])}")

assert (Solution().rotateTheBox([["#", "#", "*", ".", "*", "."],
                                 ["#", "#", "#", "*", ".", "."],
                                 ["#", "#", "#", ".", "#", "."]]) == [[".", "#", "#"],
                                                                      [".", "#", "#"],
                                                                      ["#", "#", "*"],
                                                                      ["#", "*", "."],
                                                                      ["#", ".", "*"],
                                                                      ["#", ".", "."]]), \
    (f"Expected {[[".", "#", "#"], [".", "#", "#"], ["#", "#", "*"], ["#", "*", "."],
                  ["#", ".", "*"], ["#", ".", "."]]}, "
     f"received {Solution().rotateTheBox([["#", "#", "*", ".", "*", "."],
                                          ["#", "#", "#", "*", ".", "."],
                                          ["#", "#", "#", ".", "#", "."]])}")
