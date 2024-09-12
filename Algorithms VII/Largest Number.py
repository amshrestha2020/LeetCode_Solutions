Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

 

Example 1:

Input: nums = [10,2]
Output: "210"
Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 109




from typing import List
from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def comparator(x, y):
            if x + y > y + x:
                return 1
            elif x + y < y + x:
                return -1
            else:
                return 0

        nums = [str(num) for num in nums]
        nums.sort(key=cmp_to_key(comparator), reverse=True)
        return str(int(''.join(nums)))
