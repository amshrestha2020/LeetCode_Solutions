Given an array nums of positive integers, return the longest possible length of an array prefix of nums, such that it is possible to remove exactly one element from this prefix so that every number that has appeared in it will have the same number of occurrences.

If after removing one element there are no remaining elements, it's still considered that every appeared number has the same number of ocurrences (0).

 

Example 1:

Input: nums = [2,2,1,1,5,3,3,5]
Output: 7
Explanation: For the subarray [2,2,1,1,5,3,3] of length 7, if we remove nums[4] = 5, we will get [2,2,1,1,3,3], so that each number will appear exactly twice.
Example 2:

Input: nums = [1,1,1,2,2,2,3,3,3,4,4,4,5]
Output: 13
 

Constraints:

2 <= nums.length <= 105
1 <= nums[i] <= 105




from collections import defaultdict

class Solution:
    def maxEqualFreq(self, v):
        mp = defaultdict(int)
        c = o = m = z = ans = 0
        for i in v:
            c += 1
            mp[i] += 1
            o += 1 if mp[i] == 1 else -1 if mp[i] == 2 else 0
            if mp[i] > z:
                z = mp[i]
                m = 1
            elif mp[i] == z:
                m += 1
            if ((c % len(mp) == 1 and z == c // len(mp) + 1 and o == 0 and m == 1) or 
                (len(mp) > 1 and (c - 1) % (len(mp) - 1) == 0 and o == 1 and m == len(mp) - 1) or 
                len(mp) == 1 or c - len(mp) == 1 or c == o):
                ans = max(ans, c)
        return ans

