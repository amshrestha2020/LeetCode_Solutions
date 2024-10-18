Given an integer array nums and an integer k, return the number of subarrays of nums where the greatest common divisor of the subarray's elements is k.

A subarray is a contiguous non-empty sequence of elements within an array.

The greatest common divisor of an array is the largest integer that evenly divides all the array elements.

 

Example 1:

Input: nums = [9,3,1,2,6,3], k = 3
Output: 4
Explanation: The subarrays of nums where 3 is the greatest common divisor of all the subarray's elements are:
- [9,3,1,2,6,3]
- [9,3,1,2,6,3]
- [9,3,1,2,6,3]
- [9,3,1,2,6,3]
Example 2:

Input: nums = [4], k = 7
Output: 0
Explanation: There are no subarrays of nums where 7 is the greatest common divisor of all the subarray's elements.
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i], k <= 109




class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        import math

        count = 0
        n = len(nums)
        
        # Iterate over all subarray starting points
        for i in range(n):
            current_gcd = 0
            # Iterate over all subarray ending points starting from i
            for j in range(i, n):
                # Compute the GCD of the current subarray [i...j]
                current_gcd = math.gcd(current_gcd, nums[j])
                
                # If at any point GCD becomes less than k, break early
                if current_gcd < k:
                    break
                
                # If GCD equals k, we found a valid subarray
                if current_gcd == k:
                    count += 1
        
        return count