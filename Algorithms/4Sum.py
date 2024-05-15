Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
 

Constraints:

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109



class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Sort the input array
        nums.sort()
        result = []
        
        # Iterate through the array with a fixed index i
        for i in range(len(nums) - 3):
            # Skip duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Iterate through the array with a fixed index j
            for j in range(i + 1, len(nums) - 2):
                # Skip duplicates
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                left, right = j + 1, len(nums) - 1
                while left < right:
                    # Calculate the current sum
                    current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    # If sum equals target, add to result
                    if current_sum == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        # Skip duplicates
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif current_sum < target:
                        left += 1
                    else:
                        right -= 1
        
        return result

# Test cases
solution = Solution()
print(solution.fourSum([1, 0, -1, 0, -2, 2], 0))  # Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
print(solution.fourSum([2, 2, 2, 2, 2], 8))      # Output: [[2,2,2,2]]

