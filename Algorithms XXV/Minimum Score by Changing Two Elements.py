You are given an integer array nums.

The low score of nums is the minimum absolute difference between any two integers.
The high score of nums is the maximum absolute difference between any two integers.
The score of nums is the sum of the high and low scores.
Return the minimum score after changing two elements of nums.

 

Example 1:

Input: nums = [1,4,7,8,5]

Output: 3

Explanation:

Change nums[0] and nums[1] to be 6 so that nums becomes [6,6,7,8,5].
The low score is the minimum absolute difference: |6 - 6| = 0.
The high score is the maximum absolute difference: |8 - 5| = 3.
The sum of high and low score is 3.
Example 2:

Input: nums = [1,4,3]

Output: 0

Explanation:

Change nums[1] and nums[2] to 1 so that nums becomes [1,1,1].
The sum of maximum absolute difference and minimum absolute difference is 0.
 

Constraints:

3 <= nums.length <= 105
1 <= nums[i] <= 109


class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()  # Sort the array to easily access min and max values
        n = len(nums)

        # Calculate the potential scores by changing two smallest or two largest
        # and one from each end as well

        # Change two smallest elements
        option1 = (nums[n-1] - nums[2])  # Change nums[0] and nums[1]
        
        # Change two largest elements
        option2 = (nums[n-3] - nums[0])  # Change nums[n-2] and nums[n-1]

        # Change one smallest and one largest
        option3 = (nums[n-2] - nums[1])  # Change nums[n-1] and nums[0]

        # The minimum score is the smallest of the calculated options
        return min(option1, option2, option3)        