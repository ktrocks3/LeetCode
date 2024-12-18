import heapq
from collections import Counter

from collections import Counter
import heapq


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        # Count frequency of each character
        freq = Counter(s)

        # Create a max-heap based on the negative ASCII value of characters
        heap = [(-ord(ch), ch, freq[ch]) for ch in freq]
        heapq.heapify(heap)

        result = []

        while heap:
            # Pop the lexicographically largest character
            _, char, count = heapq.heappop(heap)

            # Determine how many times we can use the character
            use_count = min(count, repeatLimit)
            result.extend([char] * use_count)

            # If there are remaining characters, handle the next largest
            count -= use_count
            if count > 0:
                if not heap:
                    # If no alternative characters exist, stop
                    break

                # Pop the next largest character
                _, next_char, next_count = heapq.heappop(heap)

                # Add one occurrence of the next character to break the sequence
                result.append(next_char)
                next_count -= 1

                # Push both characters back into the heap if they have remaining counts
                if next_count > 0:
                    heapq.heappush(heap, (-ord(next_char), next_char, next_count))
                heapq.heappush(heap, (-ord(char), char, count))

        return ''.join(result)


assert Solution().repeatLimitedString('cczazcc', 3) == "zzcccac", \
    f'Expected: "zzcccac", Received: {Solution().repeatLimitedString('cczazcc', 3)}'
assert Solution().repeatLimitedString('aababab', 2) == "bbabaa", \
    f'Expected: "bbabaa", Received: {Solution().repeatLimitedString('aababab', 2)}'
