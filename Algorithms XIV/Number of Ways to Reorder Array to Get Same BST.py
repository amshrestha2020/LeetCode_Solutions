Given an array nums that represents a permutation of integers from 1 to n. We are going to construct a binary search tree (BST) by inserting the elements of nums in order into an initially empty BST. Find the number of different ways to reorder nums so that the constructed BST is identical to that formed from the original array nums.

For example, given nums = [2,1,3], we will have 2 as the root, 1 as a left child, and 3 as a right child. The array [2,3,1] also yields the same BST but [3,2,1] yields a different BST.
Return the number of ways to reorder nums such that the BST formed is identical to the original BST formed from nums.

Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:


Input: nums = [2,1,3]
Output: 1
Explanation: We can reorder nums to be [2,3,1] which will yield the same BST. There are no other ways to reorder nums which will yield the same BST.
Example 2:


Input: nums = [3,4,5,1,2]
Output: 5
Explanation: The following 5 arrays will yield the same BST: 
[3,1,2,4,5]
[3,1,4,2,5]
[3,1,4,5,2]
[3,4,1,2,5]
[3,4,1,5,2]
Example 3:


Input: nums = [1,2,3]
Output: 0
Explanation: There are no other orderings of nums that will yield the same BST.
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= nums.length
All integers in nums are distinct.




from math import comb
from collections import deque
from functools import lru_cache

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        n = len(nums)
        fact = [1] * (n + 1)
        inv = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % mod
            inv[i] = pow(fact[i], mod - 2, mod)

        @lru_cache(None)
        def binom(n, k):
            if k < 0 or k > n:
                return 0
            return fact[n] * inv[k] * inv[n - k] % mod

        def dfs(nums):
            if len(nums) <= 2:
                return 1
            root = nums[0]
            left = [x for x in nums if x < root]
            right = [x for x in nums if x > root]
            return binom(len(left) + len(right), len(right)) * dfs(left) * dfs(right) % mod

        return (dfs(nums) - 1) % mod
