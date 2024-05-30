You are given an integer array nums that is sorted in non-decreasing order.

Determine if it is possible to split nums into one or more subsequences such that both of the following conditions are true:

Each subsequence is a consecutive increasing sequence (i.e. each integer is exactly one more than the previous integer).
All subsequences have a length of 3 or more.
Return true if you can split nums according to the above conditions, or false otherwise.

A subsequence of an array is a new array that is formed from the original array by deleting some (can be none) of the elements without disturbing the relative positions of the remaining elements. (i.e., [1,3,5] is a subsequence of [1,2,3,4,5] while [1,3,2] is not).

 

Example 1:

Input: nums = [1,2,3,3,4,5]
Output: true
Explanation: nums can be split into the following subsequences:
[1,2,3,3,4,5] --> 1, 2, 3
[1,2,3,3,4,5] --> 3, 4, 5
Example 2:

Input: nums = [1,2,3,3,4,4,5,5]
Output: true
Explanation: nums can be split into the following subsequences:
[1,2,3,3,4,4,5,5] --> 1, 2, 3, 4, 5
[1,2,3,3,4,4,5,5] --> 3, 4, 5
Example 3:

Input: nums = [1,2,3,4,4,5]
Output: false
Explanation: It is impossible to split nums into consecutive increasing subsequences of length 3 or more.
 

Constraints:

1 <= nums.length <= 104
-1000 <= nums[i] <= 1000
nums is sorted in non-decreasing order.




from typing import List
import collections
import heapq

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        # count the frequency of each number
        freq = collections.Counter(nums)
        # store the end element of each subsequence
        tails = collections.defaultdict(list)

        for num in nums:
            if freq[num] == 0:
                continue
            freq[num] -= 1

            # if num can be appended to an existing subsequence
            if tails[num - 1]:
                # remove the subsequence ending with num - 1
                length = heapq.heappop(tails[num - 1])
                # add a new subsequence ending with num
                heapq.heappush(tails[num], length + 1)
            else:
                # create a new subsequence
                heapq.heappush(tails[num], 1)

        # check if all subsequences have length >= 3
        for tail in tails.values():
            if any(length < 3 for length in tail):
                return False

        return True
