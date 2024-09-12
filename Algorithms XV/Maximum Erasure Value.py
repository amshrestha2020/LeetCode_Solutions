You are given an array of positive integers nums and want to erase a subarray containing unique elements. The score you get by erasing the subarray is equal to the sum of its elements.

Return the maximum score you can get by erasing exactly one subarray.

An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).

 

Example 1:

Input: nums = [4,2,4,5,6]
Output: 17
Explanation: The optimal subarray here is [2,4,5,6].
Example 2:

Input: nums = [5,2,1,2,5,2,1,2,5]
Output: 8
Explanation: The optimal subarray here is [5,2,1] or [1,2,5].
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 104



class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = 0
        current_sum = 0
        max_sum = 0
        unique_elements = set()
        
        for right in range(len(nums)):
            # If nums[right] is already in the set, shrink the window
            while nums[right] in unique_elements:
                unique_elements.remove(nums[left])
                current_sum -= nums[left]
                left += 1
            
            # Add the current element to the set and update the current sum
            unique_elements.add(nums[right])
            current_sum += nums[right]
            
            # Update the max_sum if the current sum is greater
            max_sum = max(max_sum, current_sum)
        
        return max_sum        