You are given two strings a and b that consist of lowercase letters. In one operation, you can change any character in a or b to any lowercase letter.

Your goal is to satisfy one of the following three conditions:

Every letter in a is strictly less than every letter in b in the alphabet.
Every letter in b is strictly less than every letter in a in the alphabet.
Both a and b consist of only one distinct letter.
Return the minimum number of operations needed to achieve your goal.

 

Example 1:

Input: a = "aba", b = "caa"
Output: 2
Explanation: Consider the best way to make each condition true:
1) Change b to "ccc" in 2 operations, then every letter in a is less than every letter in b.
2) Change a to "bbb" and b to "aaa" in 3 operations, then every letter in b is less than every letter in a.
3) Change a to "aaa" and b to "aaa" in 2 operations, then a and b consist of one distinct letter.
The best way was done in 2 operations (either condition 1 or condition 3).
Example 2:

Input: a = "dabadd", b = "cda"
Output: 3
Explanation: The best way is to make condition 1 true by changing b to "eee".
 

Constraints:

1 <= a.length, b.length <= 105
a and b consist only of lowercase letters.




class Solution:
    def minCharacters(self, a: str, b: str) -> int:

        from collections import Counter
        
        # Frequency counts of each letter in `a` and `b`
        count_a = Counter(a)
        count_b = Counter(b)
        
        # Total length of strings `a` and `b`
        len_a = len(a)
        len_b = len(b)
        
        # Calculate the minimum number of operations required for condition 3
        min_operations_condition_3 = float('inf')
        for ch in range(ord('a'), ord('z') + 1):
            char = chr(ch)
            # Convert all characters in `a` and `b` to `char`
            operations = (len_a - count_a.get(char, 0)) + (len_b - count_b.get(char, 0))
            min_operations_condition_3 = min(min_operations_condition_3, operations)
        
        # Calculate prefix sums for the counts of characters in `a` and `b`
        prefix_sum_a = [0] * 26
        prefix_sum_b = [0] * 26
        
        for i in range(26):
            char = chr(ord('a') + i)
            prefix_sum_a[i] = count_a.get(char, 0) + (prefix_sum_a[i - 1] if i > 0 else 0)
            prefix_sum_b[i] = count_b.get(char, 0) + (prefix_sum_b[i - 1] if i > 0 else 0)
        
        # Minimum operations for condition 1
        min_operations_condition_1 = float('inf')
        for i in range(25):
            operations = (prefix_sum_a[25] - prefix_sum_a[i]) + prefix_sum_b[i]
            min_operations_condition_1 = min(min_operations_condition_1, operations)
        
        # Minimum operations for condition 2
        min_operations_condition_2 = float('inf')
        for i in range(25):
            operations = (prefix_sum_b[25] - prefix_sum_b[i]) + prefix_sum_a[i]
            min_operations_condition_2 = min(min_operations_condition_2, operations)
        
        # Return the minimum number of operations needed
        return min(min_operations_condition_1, min_operations_condition_2, min_operations_condition_3)
