A magical string s consists of only '1' and '2' and obeys the following rules:

The string s is magical because concatenating the number of contiguous occurrences of characters '1' and '2' generates the string s itself.
The first few elements of s is s = "1221121221221121122……". If we group the consecutive 1's and 2's in s, it will be "1 22 11 2 1 22 1 22 11 2 11 22 ......" and the occurrences of 1's or 2's in each group are "1 2 2 1 1 2 1 2 2 1 2 2 ......". You can see that the occurrence sequence is s itself.

Given an integer n, return the number of 1's in the first n number in the magical string s.

 

Example 1:

Input: n = 6
Output: 3
Explanation: The first 6 elements of magical string s is "122112" and it contains three 1's, so return 3.
Example 2:

Input: n = 1
Output: 1
 

Constraints:

1 <= n <= 105




class Solution:
    def magicalString(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 3:
            return 1
        
        # Initialize the magical string with the first few characters
        s = [1, 2, 2]
        # Pointer to the position in the sequence that dictates the next elements
        idx = 2
        # The current value to add (alternates between 1 and 2)
        num = 1
        count_ones = 1  # Initial count of '1's (since "122" has one '1')
        
        while len(s) < n:
            # Get the number of times we need to append the current num
            times = s[idx]
            s.extend([num] * times)
            if num == 1:
                count_ones += times
            # Alternate between 1 and 2
            num = 3 - num
            # Move to the next index
            idx += 1
        
        # If the list overshoots n, adjust the count of '1's accordingly
        return count_ones if len(s) == n else count_ones - s[n:].count(1)

# Example usage:
# sol = Solution()
# print(sol.magicalString(6))  # Output: 3
# print(sol.magicalString(1))  # Output: 1
