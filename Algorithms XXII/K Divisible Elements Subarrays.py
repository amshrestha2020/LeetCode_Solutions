Given an integer array nums and two integers k and p, return the number of distinct subarrays, which have at most k elements that are divisible by p.

Two arrays nums1 and nums2 are said to be distinct if:

They are of different lengths, or
There exists at least one index i where nums1[i] != nums2[i].
A subarray is defined as a non-empty contiguous sequence of elements in an array.

 

Example 1:

Input: nums = [2,3,3,2,2], k = 2, p = 2
Output: 11
Explanation:
The elements at indices 0, 3, and 4 are divisible by p = 2.
The 11 distinct subarrays which have at most k = 2 elements divisible by 2 are:
[2], [2,3], [2,3,3], [2,3,3,2], [3], [3,3], [3,3,2], [3,3,2,2], [3,2], [3,2,2], and [2,2].
Note that the subarrays [2] and [3] occur more than once in nums, but they should each be counted only once.
The subarray [2,3,3,2,2] should not be counted because it has 3 elements that are divisible by 2.
Example 2:

Input: nums = [1,2,3,4], k = 4, p = 1
Output: 10
Explanation:
All element of nums are divisible by p = 1.
Also, every subarray of nums will have at most 4 elements that are divisible by 1.
Since all subarrays are distinct, the total number of subarrays satisfying all the constraints is 10.
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i], p <= 200
1 <= k <= nums.length
 

Follow up:

Can you solve this problem in O(n2) time complexity?




class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        from typing import List


        distinct_subarrays = set()
        n = len(nums)

        # Iterate through each starting index of the subarray
        for start in range(n):
            divisible_count = 0
            current_subarray = []

            # Iterate through each ending index of the subarray
            for end in range(start, n):
                current_subarray.append(nums[end])

                # Check if the current number is divisible by p
                if nums[end] % p == 0:
                    divisible_count += 1

                # If we exceed k divisible elements, break
                if divisible_count > k:
                    break
                
                # Add the tuple of the current subarray to the set
                distinct_subarrays.add(tuple(current_subarray))

        # The size of the set gives us the count of distinct subarrays
        return len(distinct_subarrays)