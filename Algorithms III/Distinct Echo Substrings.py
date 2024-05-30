Return the number of distinct non-empty substrings of text that can be written as the concatenation of some string with itself (i.e. it can be written as a + a where a is some string).

 

Example 1:

Input: text = "abcabcabc"
Output: 3
Explanation: The 3 substrings are "abcabc", "bcabca" and "cabcab".
Example 2:

Input: text = "leetcodeleetcode"
Output: 2
Explanation: The 2 substrings are "ee" and "leetcodeleetcode".
 

Constraints:

1 <= text.length <= 2000
text has only lowercase English letters.





class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        n = len(text)
        echo_substrings = set()
        
        # Iterate over each possible starting position
        for i in range(n):
            # Iterate over even lengths of substrings
            for length in range(2, n - i + 1, 2):
                half = length // 2
                if text[i:i+half] == text[i+half:i+length]:
                    echo_substrings.add(text[i:i+length])
        
        return len(echo_substrings)

# Example usage:
solution = Solution()
print(solution.distinctEchoSubstrings("abcabcabc"))  # Output: 3
print(solution.distinctEchoSubstrings("leetcodeleetcode"))  # Output: 2
