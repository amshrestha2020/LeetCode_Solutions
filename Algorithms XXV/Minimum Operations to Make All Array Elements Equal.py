You are given an array nums consisting of positive integers.

You are also given an integer array queries of size m. For the ith query, you want to make all of the elements of nums equal to queries[i]. You can perform the following operation on the array any number of times:

Increase or decrease an element of the array by 1.
Return an array answer of size m where answer[i] is the minimum number of operations to make all elements of nums equal to queries[i].

Note that after each query the array is reset to its original state.

 

Example 1:

Input: nums = [3,1,6,8], queries = [1,5]
Output: [14,10]
Explanation: For the first query we can do the following operations:
- Decrease nums[0] 2 times, so that nums = [1,1,6,8].
- Decrease nums[2] 5 times, so that nums = [1,1,1,8].
- Decrease nums[3] 7 times, so that nums = [1,1,1,1].
So the total number of operations for the first query is 2 + 5 + 7 = 14.
For the second query we can do the following operations:
- Increase nums[0] 2 times, so that nums = [5,1,6,8].
- Increase nums[1] 4 times, so that nums = [5,5,6,8].
- Decrease nums[2] 1 time, so that nums = [5,5,5,8].
- Decrease nums[3] 3 times, so that nums = [5,5,5,5].
So the total number of operations for the second query is 2 + 4 + 1 + 3 = 10.
Example 2:

Input: nums = [2,9,6,3], queries = [10]
Output: [20]
Explanation: We can increase each value in the array to 10. The total number of operations will be 8 + 1 + 4 + 7 = 20.
 

Constraints:

n == nums.length
m == queries.length
1 <= n, m <= 105
1 <= nums[i], queries[i] <= 109



class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        from typing import List
        import bisect

        nums.sort()
        
        # Step 2: Create a prefix sum array
        prefix_sum = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]

        # Step 3: Prepare the result for each query
        result = []
        for query in queries:
            # Use binary search to find the index where query would fit
            idx = bisect.bisect_left(nums, query)
            
            # Calculate operations needed
            operations = 0
            
            # Elements to the left of idx need to be increased to query
            if idx > 0:
                operations += query * idx - prefix_sum[idx]
            
            # Elements to the right of idx need to be decreased to query
            operations += (prefix_sum[len(nums)] - prefix_sum[idx]) - query * (len(nums) - idx)
            
            result.append(operations)
        
        return result