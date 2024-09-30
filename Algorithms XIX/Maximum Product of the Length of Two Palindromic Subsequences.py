Given a string s, find two disjoint palindromic subsequences of s such that the product of their lengths is maximized. The two subsequences are disjoint if they do not both pick a character at the same index.

Return the maximum possible product of the lengths of the two palindromic subsequences.

A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters. A string is palindromic if it reads the same forward and backward.

 

Example 1:

example-1
Input: s = "leetcodecom"
Output: 9
Explanation: An optimal solution is to choose "ete" for the 1st subsequence and "cdc" for the 2nd subsequence.
The product of their lengths is: 3 * 3 = 9.
Example 2:

Input: s = "bb"
Output: 1
Explanation: An optimal solution is to choose "b" (the first character) for the 1st subsequence and "b" (the second character) for the 2nd subsequence.
The product of their lengths is: 1 * 1 = 1.
Example 3:

Input: s = "accbcaxxcxx"
Output: 25
Explanation: An optimal solution is to choose "accca" for the 1st subsequence and "xxcxx" for the 2nd subsequence.
The product of their lengths is: 5 * 5 = 25.
 

Constraints:

2 <= s.length <= 12
s consists of lowercase English letters only.




class Solution:
    def maxProduct(self, s: str) -> int:
        def is_palindrome(subseq):
            return subseq == subseq[::-1]
        
        n = len(s)
        palindromic_subsequences = []

        # Generate all subsequences
        for mask in range(1 << n):
            subsequence = []
            for i in range(n):
                if mask & (1 << i):
                    subsequence.append(s[i])
            subsequence = ''.join(subsequence)
            if is_palindrome(subsequence):
                palindromic_subsequences.append((subsequence, mask))  # store subsequence and its bitmask

        max_product = 0
        num_palindromes = len(palindromic_subsequences)

        # Calculate max product of lengths of disjoint palindromic subsequences
        for i in range(num_palindromes):
            subseq1, mask1 = palindromic_subsequences[i]
            for j in range(i + 1, num_palindromes):
                subseq2, mask2 = palindromic_subsequences[j]
                # Check if they are disjoint
                if mask1 & mask2 == 0:
                    product = len(subseq1) * len(subseq2)
                    max_product = max(max_product, product)

        return max_product        