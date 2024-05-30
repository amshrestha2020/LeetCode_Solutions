You are given a 2D integer array intervals where intervals[i] = [starti, endi] represents all the integers from starti to endi inclusively.

A containing set is an array nums where each interval from intervals has at least two integers in nums.

For example, if intervals = [[1,3], [3,7], [8,9]], then [1,2,4,7,8,9] and [2,3,4,8,9] are containing sets.
Return the minimum possible size of a containing set.

 

Example 1:

Input: intervals = [[1,3],[3,7],[8,9]]
Output: 5
Explanation: let nums = [2, 3, 4, 8, 9].
It can be shown that there cannot be any containing array of size 4.
Example 2:

Input: intervals = [[1,3],[1,4],[2,5],[3,5]]
Output: 3
Explanation: let nums = [2, 3, 4].
It can be shown that there cannot be any containing array of size 2.
Example 3:

Input: intervals = [[1,2],[2,3],[2,4],[4,5]]
Output: 5
Explanation: let nums = [1, 2, 3, 4, 5].
It can be shown that there cannot be any containing array of size 4.
 

Constraints:

1 <= intervals.length <= 3000
intervals[i].length == 2
0 <= starti < endi <= 108



class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # Sort the intervals by their end values
        intervals.sort(key=lambda x: x[1])
        res = [-1, -1]
        for start, end in intervals:
            # If the interval does not intersect with the last two elements in res
            if start > res[-1]:
                res += [end - 1, end]
            # If the interval intersects with one of the last two elements in res
            elif start > res[-2]:
                res += [end]
            # If the interval's start is equal to the last element in res
            elif start == res[-1]:
                res += [end]
        return len(res) - 2

