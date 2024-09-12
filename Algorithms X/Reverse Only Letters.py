Given a string s, reverse the string according to the following rules:

All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.

 

Example 1:

Input: s = "ab-cd"
Output: "dc-ba"
Example 2:

Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"
 

Constraints:

1 <= s.length <= 100
s consists of characters with ASCII values in the range [33, 122].
s does not contain '\"' or '\\'.






class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        # Convert the string to a list because strings are immutable in Python
        s = list(s)
        
        # Initialize two pointers
        i, j = 0, len(s) - 1
        
        while i < j:
            # If s[i] is not an English letter, move the pointer i to the right
            if not s[i].isalpha():
                i += 1
            # If s[j] is not an English letter, move the pointer j to the left
            elif not s[j].isalpha():
                j -= 1
            else:
                # Swap s[i] and s[j]
                s[i], s[j] = s[j], s[i]
                # Move both pointers
                i += 1
                j -= 1
        
        # Convert the list back to a string
        return ''.join(s)
