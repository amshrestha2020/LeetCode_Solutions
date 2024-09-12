You are given an integer array nums.

You should move each element of nums into one of the two arrays A and B such that A and B are non-empty, and average(A) == average(B).

Return true if it is possible to achieve that and false otherwise.

Note that for an array arr, average(arr) is the sum of all the elements of arr over the length of arr.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7,8]
Output: true
Explanation: We can split the array into [1,4,5,8] and [2,3,6,7], and both of them have an average of 4.5.
Example 2:

Input: nums = [3,1]
Output: false
 

Constraints:

1 <= nums.length <= 30
0 <= nums[i] <= 104






from typing import List

class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        total = sum(nums)
        n = len(nums)
        dp = [set() for _ in range(n+1)]
        dp[0].add(0)
        for num in nums:
            for i in range(n, 0, -1):
                for prev in dp[i-1]:
                    dp[i].add(prev + num)
        for i in range(1, n):
            if total * i % n == 0 and total * i // n in dp[i]:
                return True
        return False
