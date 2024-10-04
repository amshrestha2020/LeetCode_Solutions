You are given a 0-indexed string text and another 0-indexed string pattern of length 2, both of which consist of only lowercase English letters.

You can add either pattern[0] or pattern[1] anywhere in text exactly once. Note that the character can be added even at the beginning or at the end of text.

Return the maximum number of times pattern can occur as a subsequence of the modified text.

A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

 

Example 1:

Input: text = "abdcdbc", pattern = "ac"
Output: 4
Explanation:
If we add pattern[0] = 'a' in between text[1] and text[2], we get "abadcdbc". Now, the number of times "ac" occurs as a subsequence is 4.
Some other strings which have 4 subsequences "ac" after adding a character to text are "aabdcdbc" and "abdacdbc".
However, strings such as "abdcadbc", "abdccdbc", and "abdcdbcc", although obtainable, have only 3 subsequences "ac" and are thus suboptimal.
It can be shown that it is not possible to get more than 4 subsequences "ac" by adding only one character.
Example 2:

Input: text = "aabb", pattern = "ab"
Output: 6
Explanation:
Some of the strings which can be obtained from text and have 6 subsequences "ab" are "aaabb", "aaabb", and "aabbb".
 

Constraints:

1 <= text.length <= 105
pattern.length == 2
text and pattern consist only of lowercase English letters.



class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        ans = 0
        ch1 = pattern[0]
        ch2 = pattern[1]

        # Count occurrences of ch1 and ch2 in the text
        p1 = text.count(ch1)
        p2 = text.count(ch2)

        # Append or insert the appropriate character based on the counts
        if p1 >= p2:
            text += ch2
        else:
            text = ch1 + text  # Inserting ch1 at the beginning

        count = 0  # To count occurrences of ch1
        for ch in text:
            if ch == ch2 and count:
                ans += count  # Increment ans by the count of ch1 seen so far
            count += ch == ch1  # Increment count if ch is ch1

        return ans        