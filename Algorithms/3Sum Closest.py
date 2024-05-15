Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 

Constraints:

3 <= nums.length <= 500
-1000 <= nums[i] <= 1000
-104 <= target <= 104




class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Sort the input array
        nums.sort()
        closest_sum = float('inf')
        
        # Iterate through the array with a fixed index i
        for i in range(len(nums)):
            left, right = i + 1, len(nums) - 1
            while left < right:
                # Calculate the current sum
                current_sum = nums[i] + nums[left] + nums[right]
                
                # Update closest_sum if the current sum is closer to the target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # Move pointers based on comparison with target
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return closest_sum  # Found an exact match
                
        return closest_sum

# Test cases
solution = Solution()
print(solution.threeSumClosest([-1, 2, 1, -4], 1))  # Output: 2
print(solution.threeSumClosest([0, 0, 0], 1))      # Output: 0

