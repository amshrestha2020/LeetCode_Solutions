Given two integer arrays arr1 and arr2, return the minimum number of operations (possibly zero) needed to make arr1 strictly increasing.

In one operation, you can choose two indices 0 <= i < arr1.length and 0 <= j < arr2.length and do the assignment arr1[i] = arr2[j].

If there is no way to make arr1 strictly increasing, return -1.

 

Example 1:

Input: arr1 = [1,5,3,6,7], arr2 = [1,3,2,4]
Output: 1
Explanation: Replace 5 with 2, then arr1 = [1, 2, 3, 6, 7].
Example 2:

Input: arr1 = [1,5,3,6,7], arr2 = [4,3,1]
Output: 2
Explanation: Replace 5 with 3 and then replace 3 with 4. arr1 = [1, 3, 4, 6, 7].
Example 3:

Input: arr1 = [1,5,3,6,7], arr2 = [1,6,3,3]
Output: -1
Explanation: You can't make arr1 strictly increasing.
 

Constraints:

1 <= arr1.length, arr2.length <= 2000
0 <= arr1[i], arr2[i] <= 10^9




from typing import List
import bisect

class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()
        dp = {-1: 0}
        for i in arr1:
            temp = {}
            for key in dp:
                if i > key:
                    if i not in temp or dp[key] < temp[i]:
                        temp[i] = dp[key]
                loc = bisect.bisect_right(arr2, key)
                if loc < len(arr2):
                    if arr2[loc] not in temp or dp[key] + 1 < temp[arr2[loc]]:
                        temp[arr2[loc]] = dp[key] + 1
            dp = temp
        if dp:
            return min(dp.values())
        return -1
