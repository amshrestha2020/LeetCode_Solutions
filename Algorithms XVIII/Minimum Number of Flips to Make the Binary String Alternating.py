You are given a binary string s. You are allowed to perform two types of operations on the string in any sequence:

Type-1: Remove the character at the start of the string s and append it to the end of the string.
Type-2: Pick any character in s and flip its value, i.e., if its value is '0' it becomes '1' and vice-versa.
Return the minimum number of type-2 operations you need to perform such that s becomes alternating.

The string is called alternating if no two adjacent characters are equal.

For example, the strings "010" and "1010" are alternating, while the string "0100" is not.
 

Example 1:

Input: s = "111000"
Output: 2
Explanation: Use the first operation two times to make s = "100011".
Then, use the second operation on the third and sixth elements to make s = "101010".
Example 2:

Input: s = "010"
Output: 0
Explanation: The string is already alternating.
Example 3:

Input: s = "1110"
Output: 1
Explanation: Use the second operation on the second element to make s = "1010".
 

Constraints:

1 <= s.length <= 105
s[i] is either '0' or '1'.



class Solution:
    def minFlips(self, s: str) -> int:
        length = len(s) - 1
        flip_map = {'1': '0', '0': '1'}
        s = s + s
        alt1 = '1'
        alt2 = '0'
        left = 0
        right = 0
        diff1 = 0
        diff2 = 0
        min_flips = float('inf')

        while right < len(s):
            if right > 0:
                alt1 = flip_map[alt1]
                alt2 = flip_map[alt2]

            curr = s[right]
            if curr != alt1:
                diff1 += 1
            if curr != alt2:
                diff2 += 1
            if right - left == length:
                min_flips = min(diff1, diff2, min_flips)
                if (length + 1) % 2 == 0:
                    if s[left] != flip_map[alt1]:
                        diff1 -= 1
                    if s[left] != flip_map[alt2]:
                        diff2 -= 1
                else:
                    if s[left] != alt1:
                        diff1 -= 1
                    if s[left] != alt2:
                        diff2 -= 1
                left += 1
            right += 1

        return min_flips        