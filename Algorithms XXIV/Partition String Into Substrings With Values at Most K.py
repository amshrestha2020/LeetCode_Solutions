You are given a string s consisting of digits from 1 to 9 and an integer k.

A partition of a string s is called good if:

Each digit of s is part of exactly one substring.
The value of each substring is less than or equal to k.
Return the minimum number of substrings in a good partition of s. If no good partition of s exists, return -1.

Note that:

The value of a string is its result when interpreted as an integer. For example, the value of "123" is 123 and the value of "1" is 1.
A substring is a contiguous sequence of characters within a string.
 

Example 1:

Input: s = "165462", k = 60
Output: 4
Explanation: We can partition the string into substrings "16", "54", "6", and "2". Each substring has a value less than or equal to k = 60.
It can be shown that we cannot partition the string into less than 4 substrings.
Example 2:

Input: s = "238182", k = 5
Output: -1
Explanation: There is no good partition for this string.
 

Constraints:

1 <= s.length <= 105
s[i] is a digit from '1' to '9'.
1 <= k <= 109
 


class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        n = len(s)
        count = 0  # To count the number of partitions
        i = 0  # Start of the substring
        
        while i < n:
            # Try to form the largest valid substring starting from index i
            current_substring = ""
            while i < n and int(current_substring + s[i]) <= k:
                current_substring += s[i]
                i += 1
            
            # If we could not form any valid substring, return -1
            if current_substring == "":
                return -1
            
            # Increment the partition count
            count += 1
        
        return count        