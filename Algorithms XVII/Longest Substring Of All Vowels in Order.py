A string is considered beautiful if it satisfies the following conditions:

Each of the 5 English vowels ('a', 'e', 'i', 'o', 'u') must appear at least once in it.
The letters must be sorted in alphabetical order (i.e. all 'a's before 'e's, all 'e's before 'i's, etc.).
For example, strings "aeiou" and "aaaaaaeiiiioou" are considered beautiful, but "uaeio", "aeoiu", and "aaaeeeooo" are not beautiful.

Given a string word consisting of English vowels, return the length of the longest beautiful substring of word. If no such substring exists, return 0.

A substring is a contiguous sequence of characters in a string.

 

Example 1:

Input: word = "aeiaaioaaaaeiiiiouuuooaauuaeiu"
Output: 13
Explanation: The longest beautiful substring in word is "aaaaeiiiiouuu" of length 13.
Example 2:

Input: word = "aeeeiiiioooauuuaeiou"
Output: 5
Explanation: The longest beautiful substring in word is "aeiou" of length 5.
Example 3:

Input: word = "a"
Output: 0
Explanation: There is no beautiful substring, so return 0.
 

Constraints:

1 <= word.length <= 5 * 105
word consists of characters 'a', 'e', 'i', 'o', and 'u'.





class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        # Initialize variables
        max_len = 0
        start = 0
        count = 1  # Tracks the number of distinct vowels in correct order
        
        # Iterate through the string starting from the second character
        for i in range(1, len(word)):
            # If the current character is smaller than the previous one, reset the window
            if word[i] < word[i - 1]:
                start = i
                count = 1  # Reset the count of vowels in order
            # If the current character is a new vowel in sequence, increment the count
            elif word[i] > word[i - 1]:
                count += 1
            
            # If we have seen all 5 vowels, update the maximum length
            if count == 5:
                max_len = max(max_len, i - start + 1)
        
        return max_len        