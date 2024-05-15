Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10





class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(path, counter):
            if len(path) == len(nums):
                result.append(path[:])
                return
            for num in counter:
                if counter[num] > 0:
                    path.append(num)
                    counter[num] -= 1
                    backtrack(path, counter)
                    path.pop()
                    counter[num] += 1
        
        result = []
        counter = collections.Counter(nums)
        backtrack([], counter)
        return result
