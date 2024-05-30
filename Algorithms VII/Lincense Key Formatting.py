You are given a license key represented as a string s that consists of only alphanumeric characters and dashes. The string is separated into n + 1 groups by n dashes. You are also given an integer k.

We want to reformat the string s such that each group contains exactly k characters, except for the first group, which could be shorter than k but still must contain at least one character. Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.

Return the reformatted license key.

 

Example 1:

Input: s = "5F3Z-2e-9-w", k = 4
Output: "5F3Z-2E9W"
Explanation: The string s has been split into two parts, each part has 4 characters.
Note that the two extra dashes are not needed and can be removed.
Example 2:

Input: s = "2-5g-3-J", k = 2
Output: "2-5G-3J"
Explanation: The string s has been split into three parts, each part has 2 characters except the first part as it could be shorter as mentioned above.
 

Constraints:

1 <= s.length <= 105
s consists of English letters, digits, and dashes '-'.
1 <= k <= 104




class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        # Step 1: Remove all dashes and convert to uppercase
        cleaned_s = s.replace('-', '').upper()
        
        # Step 2: Determine the length of the first group
        first_group_length = len(cleaned_s) % k
        
        # Initialize result list
        result = []
        
        # Step 3: Add the first group if it is not empty
        if first_group_length > 0:
            result.append(cleaned_s[:first_group_length])
        
        # Step 4: Add the subsequent groups of length k
        for i in range(first_group_length, len(cleaned_s), k):
            result.append(cleaned_s[i:i + k])
        
        # Step 5: Join the groups with dashes
        return '-'.join(result)

# Example usage:
# sol = Solution()
# print(sol.licenseKeyFormatting("5F3Z-2e-9-w", 4))  # Output: "5F3Z-2E9W"
# print(sol.licenseKeyFormatting("2-5g-3-J", 2))     # Output: "2-5G-3J"
