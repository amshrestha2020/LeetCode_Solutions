Given an integer array nums, return the maximum difference between two successive elements in its sorted form. If the array contains less than two elements, return 0.

You must write an algorithm that runs in linear time and uses linear extra space.

 

Example 1:

Input: nums = [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.
Example 2:

Input: nums = [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109



class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2 or min(nums) == max(nums):
            return 0

        minVal, maxVal, n = min(nums), max(nums), len(nums)
        bucketRange = max(1, (maxVal - minVal) // (n - 1))  # bucket size or gap
        bucketSize = (maxVal - minVal) // bucketRange + 1  # number of buckets

        buckets = [[None, None] for _ in range(bucketSize)]  # store min and max val in each bucket

        for num in nums:  # put numbers into buckets
            idx = (num - minVal) // bucketRange
            if buckets[idx][0] is None:
                buckets[idx][0] = buckets[idx][1] = num
            else:
                buckets[idx][0] = min(buckets[idx][0], num)
                buckets[idx][1] = max(buckets[idx][1], num)

        maxGap = 0
        prevBucket = minVal
        for i in range(bucketSize):
            if buckets[i][0] is not None:  # skip the empty buckets
                maxGap = max(maxGap, buckets[i][0] - prevBucket)
                prevBucket = buckets[i][1]

        return maxGap
