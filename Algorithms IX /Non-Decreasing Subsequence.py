Given an integer array nums, return all the different possible non-decreasing subsequences of the given array with at least two elements. You may return the answer in any order.

 

Example 1:

Input: nums = [4,6,7,7]
Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
Example 2:

Input: nums = [4,4,3,2,1]
Output: [[4,4]]
 

Constraints:

1 <= nums.length <= 15
-100 <= nums[i] <= 100




class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        if len(path) > 1:
            res.append(path[:])
        unique = set()
        for i in range(index, len(nums)):
            if nums[i] in unique:
                continue
            if not path or nums[i] >= path[-1]:
                unique.add(nums[i])
                self.dfs(nums, i + 1, path + [nums[i]], res)
