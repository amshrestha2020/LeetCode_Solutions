Given an binary array nums and an integer k, return true if all 1's are at least k places away from each other, otherwise return false.

 

Example 1:


Input: nums = [1,0,0,0,1,0,0,1], k = 2
Output: true
Explanation: Each of the 1s are at least 2 places away from each other.
Example 2:


Input: nums = [1,0,0,1,0,1], k = 2
Output: false
Explanation: The second 1 and third 1 are only one apart from each other.
 

Constraints:

1 <= nums.length <= 105
0 <= k <= nums.length
nums[i] is 0 or 1






class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        # Initialize the position of the last 1 to -k - 1
        last_one = -k - 1

        for i in range(len(nums)):
            if nums[i] == 1:
                # If the current 1 is less than k places away from the last 1, return False
                if i - last_one <= k:
                    return False
                # Update the position of the last 1
                last_one = i

        # If we finish the iteration without returning False, all 1s are at least k places away
        return True
