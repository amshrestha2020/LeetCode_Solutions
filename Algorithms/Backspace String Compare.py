Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

 

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
 

Constraints:

1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.
 

Follow up: Can you solve it in O(n) time and O(1) space?





class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # Helper function to find the next valid character index in the string
        def next_valid_char_index(string, index):
            skip = 0  # Number of backspaces encountered
            while index >= 0:
                if string[index] == '#':
                    skip += 1  # Increment skip count for a backspace
                elif skip > 0:
                    skip -= 1  # Decrement skip count for a character to be removed
                else:
                    break  # Found a valid character
                index -= 1
            return index  # Return the index of the next valid character or -1 if none found
        
        # Initialize pointers to the end of both strings
        i, j = len(s) - 1, len(t) - 1
        
        while i >= 0 or j >= 0:
            i = next_valid_char_index(s, i)  # Find the next valid character in s
            j = next_valid_char_index(t, j)  # Find the next valid character in t
            
            if i >= 0 and j >= 0 and s[i] != t[j]:  # If both valid characters are different
                return False  # Strings are not equal
            
            if (i >= 0) != (j >= 0):  # If one string has valid characters left but the other doesn't
                return False  # Strings are not equal
            
            i -= 1  # Move to the next character in s
            j -= 1  # Move to the next character in t
        
        return True  # All characters matched, strings are equal

