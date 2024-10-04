You are given a string s and an integer repeatLimit. Construct a new string repeatLimitedString using the characters of s such that no letter appears more than repeatLimit times in a row. You do not have to use all characters from s.

Return the lexicographically largest repeatLimitedString possible.

A string a is lexicographically larger than a string b if in the first position where a and b differ, string a has a letter that appears later in the alphabet than the corresponding letter in b. If the first min(a.length, b.length) characters do not differ, then the longer string is the lexicographically larger one.

 

Example 1:

Input: s = "cczazcc", repeatLimit = 3
Output: "zzcccac"
Explanation: We use all of the characters from s to construct the repeatLimitedString "zzcccac".
The letter 'a' appears at most 1 time in a row.
The letter 'c' appears at most 3 times in a row.
The letter 'z' appears at most 2 times in a row.
Hence, no letter appears more than repeatLimit times in a row and the string is a valid repeatLimitedString.
The string is the lexicographically largest repeatLimitedString possible so we return "zzcccac".
Note that the string "zzcccca" is lexicographically larger but the letter 'c' appears more than 3 times in a row, so it is not a valid repeatLimitedString.
Example 2:

Input: s = "aababab", repeatLimit = 2
Output: "bbabaa"
Explanation: We use only some of the characters from s to construct the repeatLimitedString "bbabaa". 
The letter 'a' appears at most 2 times in a row.
The letter 'b' appears at most 2 times in a row.
Hence, no letter appears more than repeatLimit times in a row and the string is a valid repeatLimitedString.
The string is the lexicographically largest repeatLimitedString possible so we return "bbabaa".
Note that the string "bbabaaa" is lexicographically larger but the letter 'a' appears more than 2 times in a row, so it is not a valid repeatLimitedString.
 

Constraints:

1 <= repeatLimit <= s.length <= 105
s consists of lowercase English letters.





class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        from collections import Counter
        import heapq

        freq = Counter(s)
        
        # Step 2: Max-heap based on characters (negative ASCII values for max heap)
        max_heap = []
        for char, count in freq.items():
            heapq.heappush(max_heap, (-ord(char), count))
        
        result = []
        
        while max_heap:
            # Step 3: Get the lexicographically largest character available
            char1, count1 = heapq.heappop(max_heap)
            char1 = chr(-char1)  # Convert back to character
            
            # Determine how many times we can use it
            use_count = min(count1, repeatLimit)
            result.append(char1 * use_count)
            
            count1 -= use_count  # Reduce the frequency of this character
            
            if count1 > 0:
                # Step 4: Try to break the sequence with the next character
                if max_heap:
                    # Get the next lexicographically largest character
                    char2, count2 = heapq.heappop(max_heap)
                    char2 = chr(-char2)
                    
                    # Use one occurrence of this character to break the repetition
                    result.append(char2)
                    count2 -= 1  # Reduce its frequency

                    # Push it back if it still has occurrences
                    if count2 > 0:
                        heapq.heappush(max_heap, (-ord(char2), count2))
                    
                    # Push the first character back for future use
                    heapq.heappush(max_heap, (-ord(char1), count1))
                else:
                    # If there is no other character to break the sequence, we're done
                    break
        
        return ''.join(result)