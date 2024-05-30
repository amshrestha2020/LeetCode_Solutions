You are given an integer n. We reorder the digits in any order (including the original order) such that the leading digit is not zero.

Return true if and only if we can do this so that the resulting number is a power of two.

 

Example 1:

Input: n = 1
Output: true
Example 2:

Input: n = 10
Output: false
 

Constraints:

1 <= n <= 109







class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        # Convert the integer to a sorted string
        sorted_n = "".join(sorted(str(n)))
        # Check all powers of 2 with the same number of digits
        for i in range(31):  # 2**30 is the largest power of 2 with at most 10 digits
            # If the sorted string of the power of 2 matches the sorted string of n, return True
            if "".join(sorted(str(1 << i))) == sorted_n:
                return True
        # If no match is found, return False
        return False
