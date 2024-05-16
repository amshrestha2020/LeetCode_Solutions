Given an integer array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

You may assume the input array always has a valid answer.

 

Example 1:

Input: nums = [1,5,1,1,6,4]
Output: [1,6,1,5,1,4]
Explanation: [1,4,1,5,1,6] is also accepted.
Example 2:

Input: nums = [1,3,2,2,3,1]
Output: [2,3,1,3,1,2]
 

Constraints:

1 <= nums.length <= 5 * 104
0 <= nums[i] <= 5000
It is guaranteed that there will be an answer for the given input nums.
 

Follow Up: Can you do it in O(n) time and/or in-place with O(1) extra space?




class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        def findKthLargest(nums, k):
            left, right = 0, len(nums) - 1
            while True:
                pos = partition(nums, left, right)
                if pos == k - 1:
                    return nums[pos]
                if pos > k - 1:
                    right = pos - 1
                else:
                    left = pos + 1

        def partition(nums, left, right):
            pivot = nums[left]
            l, r = left + 1, right
            while l <= r:
                if nums[l] < pivot and nums[r] > pivot:
                    nums[l], nums[r] = nums[r], nums[l]
                if nums[l] >= pivot:
                    l += 1
                if nums[r] <= pivot:
                    r -= 1
            nums[left], nums[r] = nums[r], nums[left]
            return r

        def wiggleIndex(i, n):
            return (1 + 2 * i) % (n | 1)

        n = len(nums)
        mid = findKthLargest(nums, (n + 1) // 2)
        i, j, k = 0, 0, n - 1
        while j <= k:
            if nums[wiggleIndex(j, n)] > mid:
                nums[wiggleIndex(i, n)], nums[wiggleIndex(j, n)] = nums[wiggleIndex(j, n)], nums[wiggleIndex(i, n)]
                i += 1
                j += 1
            elif nums[wiggleIndex(j, n)] < mid:
                nums[wiggleIndex(j, n)], nums[wiggleIndex(k, n)] = nums[wiggleIndex(k, n)], nums[wiggleIndex(j, n)]
                k -= 1
            else:
                j += 1
