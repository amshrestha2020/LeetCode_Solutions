The bitwise AND of an array nums is the bitwise AND of all integers in nums.

For example, for nums = [1, 5, 3], the bitwise AND is equal to 1 & 5 & 3 = 1.
Also, for nums = [7], the bitwise AND is 7.
You are given an array of positive integers candidates. Evaluate the bitwise AND of every combination of numbers of candidates. Each number in candidates may only be used once in each combination.

Return the size of the largest combination of candidates with a bitwise AND greater than 0.

 

Example 1:

Input: candidates = [16,17,71,62,12,24,14]
Output: 4
Explanation: The combination [16,17,62,24] has a bitwise AND of 16 & 17 & 62 & 24 = 16 > 0.
The size of the combination is 4.
It can be shown that no combination with a size greater than 4 has a bitwise AND greater than 0.
Note that more than one combination may have the largest size.
For example, the combination [62,12,24,14] has a bitwise AND of 62 & 12 & 24 & 14 = 8 > 0.
Example 2:

Input: candidates = [8,8]
Output: 2
Explanation: The largest combination [8,8] has a bitwise AND of 8 & 8 = 8 > 0.
The size of the combination is 2, so we return 2.
 

Constraints:

1 <= candidates.length <= 105
1 <= candidates[i] <= 107





class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        from typing import List


        max_combination_size = 0
        
        # Iterate over all possible bit positions (0 to 30)
        for bit in range(31):  # 31 bits cover values up to 2^30
            count = 0
            for number in candidates:
                # Check if the bit-th bit is set
                if number & (1 << bit):
                    count += 1
            
            # Update the maximum size of combination found
            max_combination_size = max(max_combination_size, count)
        
        return max_combination_size