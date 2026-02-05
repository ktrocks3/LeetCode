import heapq
from collections import defaultdict
from typing import List


class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        # Then we need to pick k-1 items from a window of size dist+1 in nums[1:]
        target_count = k - 1
        window_size = dist + 1
        initial_window = nums[1: dist + 2]

        # Max-heap for the smallest 'target_count' elements (store as negative for max-heap behavior)
        # Min-heap for the rest of the elements in the window
        L = []  # Stores -value
        R = []  # Stores value

        # Sort initial window to distribute easily
        sorted_window = sorted(initial_window)

        current_sum = 0

        # Fill heaps initially
        for x in sorted_window[:target_count]:
            heapq.heappush(L, -x)
            current_sum += x

        for x in sorted_window[target_count:]:
            heapq.heappush(R, x)

        min_sum = current_sum

        # Map to track elements that need to be removed (lazy deletion)
        # We track counts because duplicates can exist
        out_map_L = defaultdict(int)
        out_map_R = defaultdict(int)

        # Helper to clean top of heaps
        def clean_heap(heap, out_map, is_max_heap):
            while heap:
                val = -heap[0] if is_max_heap else heap[0]
                if out_map[val] > 0:
                    out_map[val] -= 1
                    heapq.heappop(heap)
                else:
                    break

        # Slide the window
        # i is the index of the element LEAVING the window
        # j is the index of the element ENTERING the window
        n = len(nums)
        for i in range(1, n - window_size):
            out_elem = nums[i]
            in_elem = nums[i + window_size]

            # --- REMOVE Phase ---
            # Check if out_elem is currently in L (part of sum) or R
            # We assume it's in L if it's <= the largest element in L (top of max-heap)
            # However, due to lazy deletion, top of L might be stale. Clean it first.
            clean_heap(L, out_map_L, True)

            if L and out_elem <= -L[0]:
                # It was contributing to the sum
                current_sum -= out_elem
                out_map_L[out_elem] += 1
                # We logically decremented size of L, need to refill later
                need_refill = True
            else:
                # It was in R
                out_map_R[out_elem] += 1
                need_refill = False

            # --- ADD Phase ---
            # Push new element. We tentatively verify against L's bound.
            clean_heap(L, out_map_L, True)  # Clean again to be safe

            if L and in_elem < -L[0]:
                heapq.heappush(L, -in_elem)
                current_sum += in_elem
            else:
                heapq.heappush(R, in_elem)

            # Maintain exactly 'target_count' valid elements in L

            # If we removed from L (need_refill) but added to R, we must move one from R to L
            # If we removed from L and added to L, size is fine.
            # If we removed from R and added to L, L has one too many.

            # Case 1: L is missing one element (removed from L, added to R)
            if need_refill and (not L or in_elem >= -L[0]):
                clean_heap(R, out_map_R, False)
                if R:
                    move = heapq.heappop(R)
                    heapq.heappush(L, -move)
                    current_sum += move

            # Case 2: L has one extra element (removed from R, added to L)
            elif not need_refill and L and in_elem < -L[0]:
                clean_heap(L, out_map_L, True)
                move = -heapq.heappop(L)
                heapq.heappush(R, move)
                current_sum -= move

            # Update global min
            if current_sum < min_sum:
                min_sum = current_sum

        return nums[0] + min_sum

assert Solution().minimumCost([1, 3, 2, 6, 4, 2], 3, 3) == 5, \
    f'Expected: 5, Received: {Solution().minimumCost([1, 3, 2, 6, 4, 2], 3, 3)}'
assert Solution().minimumCost([10, 1, 2, 2, 2, 1], 4, 3) == 15, \
    f'Expected: 15, Received: {Solution().minimumCost([10, 1, 2, 2, 2, 1], 4, 3)}'
assert Solution().minimumCost([10, 8, 18, 9], 3, 1) == 36, \
    f'Expected: 36, Received: {Solution().minimumCost([10, 8, 18, 9], 3, 1)}'
