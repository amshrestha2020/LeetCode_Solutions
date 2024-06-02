Given an array of integers nums, find the maximum length of a subarray where the product of all its elements is positive.

A subarray of an array is a consecutive sequence of zero or more values taken out of that array.

Return the maximum length of a subarray with positive product.

 

Example 1:

Input: nums = [1,-2,-3,4]
Output: 4
Explanation: The array nums already has a positive product of 24.
Example 2:

Input: nums = [0,1,-2,-3,-4]
Output: 3
Explanation: The longest subarray with positive product is [1,-2,-3] which has a product of 6.
Notice that we cannot include 0 in the subarray since that'll make the product 0 which is not positive.
Example 3:

Input: nums = [-1,-2,-3,0,1]
Output: 2
Explanation: The longest subarray with positive product is [-1,-2] or [-2,-3].
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109




class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        max_len = 0
        pos_len = 0  # Length of subarray with positive product
        neg_len = 0  # Length of subarray with negative product
        
        for num in nums:
            if num > 0:
                pos_len += 1
                neg_len = neg_len + 1 if neg_len > 0 else 0
            elif num < 0:
                new_pos_len = neg_len + 1 if neg_len > 0 else 0
                neg_len = pos_len + 1
                pos_len = new_pos_len
            else:
                pos_len = 0
                neg_len = 0
            
            max_len = max(max_len, pos_len)
        
        return max_len
