from typing import List

class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        # def sieve(n):
        #     A = [True] * n
        #     A[0] = A[1] = False  # 0 and 1 are not prime numbers
        #     for i in range(2, int(n ** 0.5) + 1):
        #         if A[i]:
        #             for k in range(i * i, n, i):
        #                 A[k] = False
        #     return [index for index, is_prime in enumerate(A) if is_prime]
        #
        # primes = sieve(1000)
        # primes.append(0)
        # Sieves are efficent, precomputing is O(1):
        primes = [
            2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67,
            71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149,
            151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
            233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313,
            317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409,
            419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499,
            503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601,
            607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691,
            701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809,
            811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907,
            911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 0
        ]


        def binSearch(val):
            # Use binary search to find the largest prime less than `val`
            low, high = 0, len(primes) - 2
            while low <= high:
                mid = (low + high) // 2
                if primes[mid] < val:
                    low = mid + 1
                else:
                    high = mid - 1
            return high  # Returns the index of the largest prime < val closest

        nums[0] -= primes[binSearch(nums[0])]
        # Loop through nums, trying to ensure it is strictly increasing
        for i in range(1,   len(nums)):
            # Find the largest prime we can subtract from nums[i] to keep it below nums[i+1]
            prime_index = binSearch(nums[i])
            while prime_index >= 0 and (nums[i] - primes[prime_index] <= nums[i - 1]):
                prime_index -= 1

            # If no valid prime was found, it's not possible to make nums strictly increasing
            if prime_index < 0:
                continue

            # Subtract the prime from nums[i]
            nums[i] -= primes[prime_index]

        # Finally, check if nums is now strictly increasing
        return all(nums[i] < nums[i + 1] for i in range(len(nums) - 1))

# Testing the function with given examples
assert Solution().primeSubOperation([4, 9, 6, 10])
assert Solution().primeSubOperation([6, 8, 11, 12])
assert not Solution().primeSubOperation([5, 8, 3])
assert Solution().primeSubOperation([998, 2])
assert not Solution().primeSubOperation([2, 2])
