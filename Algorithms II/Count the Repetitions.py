We define str = [s, n] as the string str which consists of the string s concatenated n times.

For example, str == ["abc", 3] =="abcabcabc".
We define that string s1 can be obtained from string s2 if we can remove some characters from s2 such that it becomes s1.

For example, s1 = "abc" can be obtained from s2 = "abdbec" based on our definition by removing the bolded underlined characters.
You are given two strings s1 and s2 and two integers n1 and n2. You have the two strings str1 = [s1, n1] and str2 = [s2, n2].

Return the maximum integer m such that str = [str2, m] can be obtained from str1.

 

Example 1:

Input: s1 = "acb", n1 = 4, s2 = "ab", n2 = 2
Output: 2
Example 2:

Input: s1 = "acb", n1 = 1, s2 = "acb", n2 = 1
Output: 1
 

Constraints:

1 <= s1.length, s2.length <= 100
s1 and s2 consist of lowercase English letters.
1 <= n1, n2 <= 106




class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        if n1 == 0:
            return 0
        
        # Counters for occurrences of s2 in s1
        s1_count, s2_count = 0, 0
        # Positions tracking
        index_s2 = 0
        # Dictionary to detect cycles
        recall = {}
        
        while s1_count < n1:
            for char in s1:
                if char == s2[index_s2]:
                    index_s2 += 1
                    if index_s2 == len(s2):
                        s2_count += 1
                        index_s2 = 0
            
            s1_count += 1
            
            # Detect cycles
            if index_s2 in recall:
                s1_prev_count, s2_prev_count = recall[index_s2]
                pre_loop = (s1_prev_count, s2_prev_count)
                in_loop = (s1_count - s1_prev_count, s2_count - s2_prev_count)
                break
            else:
                recall[index_s2] = (s1_count, s2_count)
        else:
            # If no cycle is found
            return s2_count // n2
        
        # Calculate the result with the found loop
        result = pre_loop[1] + (n1 - pre_loop[0]) // in_loop[0] * in_loop[1]
        
        # Extra strings remaining after the loop
        remaining_s1_count = (n1 - pre_loop[0]) % in_loop[0]
        
        for _ in range(remaining_s1_count):
            for char in s1:
                if char == s2[index_s2]:
                    index_s2 += 1
                    if index_s2 == len(s2):
                        result += 1
                        index_s2 = 0
        
        return result // n2

# Example usage:
# sol = Solution()
# print(sol.getMaxRepetitions("acb", 4, "ab", 2))  # Output: 2
# print(sol.getMaxRepetitions("acb", 1, "acb", 1))  # Output: 1
