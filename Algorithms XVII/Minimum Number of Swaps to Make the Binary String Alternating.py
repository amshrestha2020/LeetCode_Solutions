Given a binary string s, return the minimum number of character swaps to make it alternating, or -1 if it is impossible.

The string is called alternating if no two adjacent characters are equal. For example, the strings "010" and "1010" are alternating, while the string "0100" is not.

Any two characters may be swapped, even if they are not adjacent.

 

Example 1:

Input: s = "111000"
Output: 1
Explanation: Swap positions 1 and 4: "111000" -> "101010"
The string is now alternating.
Example 2:

Input: s = "010"
Output: 0
Explanation: The string is already alternating, no swaps are needed.
Example 3:

Input: s = "1110"
Output: -1
 

Constraints:

1 <= s.length <= 1000
s[i] is either '0' or '1'.



class Solution:
    def minSwaps(self, s: str) -> int:
        n = len(s)
        
        # Define the two possible alternating patterns
        pattern1 = ''.join(['0' if i % 2 == 0 else '1' for i in range(n)])
        pattern2 = ''.join(['1' if i % 2 == 0 else '0' for i in range(n)])
        
        def count_swaps(pattern):
            # Count misplaced '0's and '1's
            mismatch_0 = mismatch_1 = 0
            for i in range(n):
                if s[i] != pattern[i]:
                    if pattern[i] == '0':
                        mismatch_0 += 1
                    else:
                        mismatch_1 += 1
            # Swaps needed is the maximum of the mismatched counts
            if mismatch_0 == mismatch_1:
                return mismatch_0
            return -1
        
        # Calculate swaps for both patterns
        swaps1 = count_swaps(pattern1)
        swaps2 = count_swaps(pattern2)
        
        # Return the minimum valid swap count or -1 if not possible
        if swaps1 == -1 and swaps2 == -1:
            return -1
        if swaps1 == -1:
            return swaps2
        if swaps2 == -1:
            return swaps1
        return min(swaps1, swaps2)        