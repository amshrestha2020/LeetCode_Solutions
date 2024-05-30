Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

 

Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: words = ["cool","lock","cook"]
Output: ["c","o"]
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of lowercase English letters.




class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        from collections import Counter

        # Initialize the counter with the first word
        count = Counter(words[0])

        # Update the counter with the intersection of the current count and the next word's count
        for word in words[1:]:
            count &= Counter(word)

        # Convert the counter to a list of characters
        return list(count.elements())
