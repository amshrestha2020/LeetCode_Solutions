The minimum absolute difference of an array a is defined as the minimum value of |a[i] - a[j]|, where 0 <= i < j < a.length and a[i] != a[j]. If all elements of a are the same, the minimum absolute difference is -1.

For example, the minimum absolute difference of the array [5,2,3,7,2] is |2 - 3| = 1. Note that it is not 0 because a[i] and a[j] must be different.
You are given an integer array nums and the array queries where queries[i] = [li, ri]. For each query i, compute the minimum absolute difference of the subarray nums[li...ri] containing the elements of nums between the 0-based indices li and ri (inclusive).

Return an array ans where ans[i] is the answer to the ith query.

A subarray is a contiguous sequence of elements in an array.

The value of |x| is defined as:

x if x >= 0.
-x if x < 0.
 

Example 1:

Input: nums = [1,3,4,8], queries = [[0,1],[1,2],[2,3],[0,3]]
Output: [2,1,4,1]
Explanation: The queries are processed as follows:
- queries[0] = [0,1]: The subarray is [1,3] and the minimum absolute difference is |1-3| = 2.
- queries[1] = [1,2]: The subarray is [3,4] and the minimum absolute difference is |3-4| = 1.
- queries[2] = [2,3]: The subarray is [4,8] and the minimum absolute difference is |4-8| = 4.
- queries[3] = [0,3]: The subarray is [1,3,4,8] and the minimum absolute difference is |3-4| = 1.
Example 2:

Input: nums = [4,5,2,2,7,10], queries = [[2,3],[0,2],[0,5],[3,5]]
Output: [-1,1,1,3]
Explanation: The queries are processed as follows:
- queries[0] = [2,3]: The subarray is [2,2] and the minimum absolute difference is -1 because all the
  elements are the same.
- queries[1] = [0,2]: The subarray is [4,5,2] and the minimum absolute difference is |4-5| = 1.
- queries[2] = [0,5]: The subarray is [4,5,2,2,7,10] and the minimum absolute difference is |4-5| = 1.
- queries[3] = [3,5]: The subarray is [2,7,10] and the minimum absolute difference is |7-10| = 3.
 

Constraints:

2 <= nums.length <= 105
1 <= nums[i] <= 100
1 <= queries.length <= 2 * 104
0 <= li < ri < nums.length





class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # We have numbers in the range 1 to 100, so we need to track frequencies for these numbers.
        MAX_NUM = 100
        n = len(nums)
        
        # Create a prefix frequency array for numbers 1 through 100
        freq = [[0] * (n + 1) for _ in range(MAX_NUM + 1)]
        
        # Fill the frequency prefix sum array
        for i in range(n):
            for num in range(1, MAX_NUM + 1):
                freq[num][i + 1] = freq[num][i]
            freq[nums[i]][i + 1] += 1
        
        result = []
        
        # Process each query
        for l, r in queries:
            present_nums = []
            
            # Collect all numbers that have non-zero frequency in the range [l, r]
            for num in range(1, MAX_NUM + 1):
                if freq[num][r + 1] - freq[num][l] > 0:
                    present_nums.append(num)
            
            # If all elements in the subarray are the same, return -1
            if len(present_nums) == 1:
                result.append(-1)
            else:
                # Calculate the minimum absolute difference between consecutive elements
                min_diff = float('inf')
                for i in range(1, len(present_nums)):
                    min_diff = min(min_diff, present_nums[i] - present_nums[i - 1])
                result.append(min_diff)
        
        return result        