You are given a string s consisting only of characters 'a' and 'b'​​​​.

You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.

Return the minimum number of deletions needed to make s balanced.

 

Example 1:

Input: s = "aababbab"
Output: 2
Explanation: You can either:
Delete the characters at 0-indexed positions 2 and 6 ("aababbab" -> "aaabbb"), or
Delete the characters at 0-indexed positions 3 and 6 ("aababbab" -> "aabbbb").
Example 2:

Input: s = "bbaaaaabb"
Output: 2
Explanation: The only solution is to delete the first two characters.
 

Constraints:

1 <= s.length <= 105
s[i] is 'a' or 'b'​​.


class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        left_b_count = [0] * n
        right_a_count = [0] * n
        
        # Count the number of 'b's to the left of each position
        count_b = 0
        for i in range(n):
            left_b_count[i] = count_b
            if s[i] == 'b':
                count_b += 1
        
        # Count the number of 'a's to the right of each position
        count_a = 0
        for i in range(n-1, -1, -1):
            right_a_count[i] = count_a
            if s[i] == 'a':
                count_a += 1
        
        # Find the minimum deletions needed
        min_deletions = float('inf')
        for i in range(n):
            min_deletions = min(min_deletions, left_b_count[i] + right_a_count[i])
        
        return min_deletions

