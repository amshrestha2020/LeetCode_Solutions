Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.

 

Example 1:

Input: s = "aab"
Output: "aba"
Example 2:

Input: s = "aaab"
Output: ""
 

Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.




import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        # Count the frequency of each character
        counter = Counter(s)
        # Create a max heap
        max_heap = [(-freq, char) for char, freq in counter.items()]
        heapq.heapify(max_heap)
        
        res = []
        while len(max_heap) > 1:
            # Pop the two most frequent characters
            freq1, char1 = heapq.heappop(max_heap)
            freq2, char2 = heapq.heappop(max_heap)
            # Add them to the result
            res.extend([char1, char2])
            # Push them back into the heap with decreased count
            if abs(freq1) > 1:
                heapq.heappush(max_heap, (freq1 + 1, char1))
            if abs(freq2) > 1:
                heapq.heappush(max_heap, (freq2 + 1, char2))
        
        # If there is still a character left in the heap
        if max_heap:
            freq, char = heapq.heappop(max_heap)
            # If its count is more than 1, return an empty string
            if abs(freq) > 1:
                return ""
            res.append(char)
        
        # Join the result list to get the final string
        return "".join(res)
