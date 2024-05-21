Given an integer array nums, partition it into two (contiguous) subarrays left and right so that:

Every element in left is less than or equal to every element in right.
left and right are non-empty.
left has the smallest possible size.
Return the length of left after such a partitioning.

Test cases are generated such that partitioning exists.

 

Example 1:

Input: nums = [5,0,3,8,6]
Output: 3
Explanation: left = [5,0,3], right = [8,6]
Example 2:

Input: nums = [1,1,1,0,6,12]
Output: 4
Explanation: left = [1,1,1,0], right = [6,12]
 

Constraints:

2 <= nums.length <= 105
0 <= nums[i] <= 106
There is at least one valid answer for the given input.




from typing import List

class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        max_left = [0] * n
        min_right = [0] * n

        m = nums[0]
        for i in range(n):
            m = max(m, nums[i])
            max_left[i] = m

        m = nums[-1]
        for i in range(n - 1, -1, -1):
            m = min(m, nums[i])
            min_right[i] = m

        for i in range(1, n):
            if max_left[i - 1] <= min_right[i]:
                return i

        return -1  # This line should never be reached because the problem guarantees that there is at least one valid answer.
