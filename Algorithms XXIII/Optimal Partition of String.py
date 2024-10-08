Given a string s, partition the string into one or more substrings such that the characters in each substring are unique. That is, no letter appears in a single substring more than once.

Return the minimum number of substrings in such a partition.

Note that each character should belong to exactly one substring in a partition.

 

Example 1:

Input: s = "abacaba"
Output: 4
Explanation:
Two possible partitions are ("a","ba","cab","a") and ("ab","a","ca","ba").
It can be shown that 4 is the minimum number of substrings needed.
Example 2:

Input: s = "ssssss"
Output: 6
Explanation:
The only valid partition is ("s","s","s","s","s","s").
 

Constraints:

1 <= s.length <= 105
s consists of only English lowercase letters.





class Solution:
    def partitionString(self, s: str) -> int:
        seen = set()  # Set to track characters in the current substring
        substring_count = 0  # Counter for the number of substrings
        
        for char in s:
            if char in seen:  # If the character is already seen, we need to start a new substring
                substring_count += 1  # Increment the count for a new substring
                seen.clear()  # Clear the set for the new substring
            
            seen.add(char)  # Add the character to the set
        
        # Add one for the last substring if any characters are left in the set
        substring_count += 1 if seen else 0
        
        return substring_count
