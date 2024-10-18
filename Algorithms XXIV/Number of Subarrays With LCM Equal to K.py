Given an integer array nums and an integer k, return the number of subarrays of nums where the least common multiple of the subarray's elements is k.

A subarray is a contiguous non-empty sequence of elements within an array.

The least common multiple of an array is the smallest positive integer that is divisible by all the array elements.

 

Example 1:

Input: nums = [3,6,2,7,1], k = 6
Output: 4
Explanation: The subarrays of nums where 6 is the least common multiple of all the subarray's elements are:
- [3,6,2,7,1]
- [3,6,2,7,1]
- [3,6,2,7,1]
- [3,6,2,7,1]
Example 2:

Input: nums = [3], k = 2
Output: 0
Explanation: There are no subarrays of nums where 2 is the least common multiple of all the subarray's elements.
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i], k <= 1000



class Solution:
    def lcm(self, a: int, b: int) -> int:
        from math import gcd
        from typing import List        


        return a * b // gcd(a, b)
    
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        
        # Iterate over all possible starting points
        for i in range(n):
            current_lcm = nums[i]
            # If the first element of the subarray is greater than k, skip it
            if current_lcm > k:
                continue
            # Check the subarray starting at index i
            for j in range(i, n):
                # Calculate the LCM of the current subarray
                current_lcm = self.lcm(current_lcm, nums[j])
                # If the LCM exceeds k, we can break early
                if current_lcm > k:
                    break
                # If the LCM matches k, count this subarray
                if current_lcm == k:
                    count += 1
        
        return count