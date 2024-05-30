Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.

 

Example 1:

Input: nums = [4,3,2,3,5,2,1], k = 4
Output: true
Explanation: It is possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
Example 2:

Input: nums = [1,2,3,4], k = 3
Output: false
 

Constraints:

1 <= k <= nums.length <= 16
1 <= nums[i] <= 104
The frequency of each element is in the range [1, 4].



from typing import List

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum = sum(nums)
        target, remainder = divmod(total_sum, k)
        
        if remainder != 0 or max(nums) > target:
            return False
        
        memo = {}
        nums.sort(reverse=True)
        
        def backtrack(used, in_progress, remaining_buckets):
            if remaining_buckets == 0:
                return True
            if in_progress == target:
                return backtrack(used, 0, remaining_buckets - 1)
            
            if used in memo:
                return memo[used]
            
            for i, num in enumerate(nums):
                if (used >> i) & 1 == 0 and in_progress + num <= target:
                    if backtrack(used | (1 << i), in_progress + num, remaining_buckets):
                        memo[used] = True
                        return True
            
            memo[used] = False
            return False
        
        return backtrack(0, 0, k)

# Test cases
solution = Solution()
print(solution.canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4))  # Output: True
print(solution.canPartitionKSubsets([1, 2, 3, 4], 3))           # Output: False
