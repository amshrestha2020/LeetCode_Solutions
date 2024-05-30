An array is squareful if the sum of every pair of adjacent elements is a perfect square.

Given an integer array nums, return the number of permutations of nums that are squareful.

Two permutations perm1 and perm2 are different if there is some index i such that perm1[i] != perm2[i].

 

Example 1:

Input: nums = [1,17,8]
Output: 2
Explanation: [1,8,17] and [17,8,1] are the valid permutations.
Example 2:

Input: nums = [2,2,2]
Output: 1
 

Constraints:

1 <= nums.length <= 12
0 <= nums[i] <= 109




from collections import Counter
from math import isqrt

class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        c = Counter(nums)
        cand = {i: {j for j in c if int((i + j)**0.5) ** 2 == i + j} for i in c}
        self.res = 0

        def dfs(x, left=len(nums) - 1):
            c[x] -= 1
            if left == 0: self.res += 1
            for y in cand[x]:
                if c[y]: dfs(y, left - 1)
            c[x] += 1

        for x in c: dfs(x)
        return self.res
