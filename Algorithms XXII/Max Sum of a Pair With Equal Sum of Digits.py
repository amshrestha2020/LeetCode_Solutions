You are given a 0-indexed array nums consisting of positive integers. You can choose two indices i and j, such that i != j, and the sum of digits of the number nums[i] is equal to that of nums[j].

Return the maximum value of nums[i] + nums[j] that you can obtain over all possible indices i and j that satisfy the conditions.

 

Example 1:

Input: nums = [18,43,36,13,7]
Output: 54
Explanation: The pairs (i, j) that satisfy the conditions are:
- (0, 2), both numbers have a sum of digits equal to 9, and their sum is 18 + 36 = 54.
- (1, 4), both numbers have a sum of digits equal to 7, and their sum is 43 + 7 = 50.
So the maximum sum that we can obtain is 54.
Example 2:

Input: nums = [10,12,19,14]
Output: -1
Explanation: There are no two numbers that satisfy the conditions, so we return -1.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109




class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        from typing import List
        from collections import defaultdict 

        def digit_sum(n: int) -> int:
            return sum(int(digit) for digit in str(n))
        
        # Dictionary to hold lists of numbers grouped by their digit sums
        sum_map = defaultdict(list)
        
        # Populate the sum_map with numbers based on their digit sums
        for num in nums:
            s = digit_sum(num)
            sum_map[s].append(num)
        
        max_sum = -1
        
        # Iterate through the sum_map to find the maximum sum of pairs
        for num_list in sum_map.values():
            if len(num_list) >= 2:  # We need at least two numbers to form a pair
                # Sort the numbers in descending order to easily find the two largest
                num_list.sort(reverse=True)
                current_sum = num_list[0] + num_list[1]  # The two largest numbers
                max_sum = max(max_sum, current_sum)
        
        return max_sum               