You are given a 0-indexed integer array nums of size n and a positive integer k.

We call an index i in the range k <= i < n - k good if the following conditions are satisfied:

The k elements that are just before the index i are in non-increasing order.
The k elements that are just after the index i are in non-decreasing order.
Return an array of all good indices sorted in increasing order.

 

Example 1:

Input: nums = [2,1,1,1,3,4,1], k = 2
Output: [2,3]
Explanation: There are two good indices in the array:
- Index 2. The subarray [2,1] is in non-increasing order, and the subarray [1,3] is in non-decreasing order.
- Index 3. The subarray [1,1] is in non-increasing order, and the subarray [3,4] is in non-decreasing order.
Note that the index 4 is not good because [4,1] is not non-decreasing.
Example 2:

Input: nums = [2,1,1,2], k = 2
Output: []
Explanation: There are no good indices in this array.
 

Constraints:

n == nums.length
3 <= n <= 105
1 <= nums[i] <= 106
1 <= k <= n / 2





class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        from typing import List

        res = []
        before = 0
        after = 0

        for i in range(k, len(nums) - k):
            # Check the k elements before
            j = max(before, i - k)
            while j < i - 1:
                if nums[j] < nums[j + 1]:
                    i = j + k
                    break  # Move to the next iteration of the outer loop
                j += 1
            else:
                # Check the k elements after
                j = max(after, i + 1)
                while j < i + k:
                    if nums[j] > nums[j + 1]:
                        i = j - 1
                        break  # Move to the next iteration of the outer loop
                    j += 1
                else:
                    # Both conditions satisfied, update before and after variables
                    before = i - 1
                    after = i + k - 1
                    res.append(i)

        return res
