You are given two positive 0-indexed integer arrays nums1 and nums2, both of length n.

The sum of squared difference of arrays nums1 and nums2 is defined as the sum of (nums1[i] - nums2[i])2 for each 0 <= i < n.

You are also given two positive integers k1 and k2. You can modify any of the elements of nums1 by +1 or -1 at most k1 times. Similarly, you can modify any of the elements of nums2 by +1 or -1 at most k2 times.

Return the minimum sum of squared difference after modifying array nums1 at most k1 times and modifying array nums2 at most k2 times.

Note: You are allowed to modify the array elements to become negative integers.

 

Example 1:

Input: nums1 = [1,2,3,4], nums2 = [2,10,20,19], k1 = 0, k2 = 0
Output: 579
Explanation: The elements in nums1 and nums2 cannot be modified because k1 = 0 and k2 = 0. 
The sum of square difference will be: (1 - 2)2 + (2 - 10)2 + (3 - 20)2 + (4 - 19)2 = 579.
Example 2:

Input: nums1 = [1,4,10,12], nums2 = [5,8,6,9], k1 = 1, k2 = 1
Output: 43
Explanation: One way to obtain the minimum sum of square difference is: 
- Increase nums1[0] once.
- Increase nums2[2] once.
The minimum of the sum of square difference will be: 
(2 - 5)2 + (4 - 8)2 + (10 - 7)2 + (12 - 9)2 = 43.
Note that, there are other ways to obtain the minimum of the sum of square difference, but there is no way to obtain a sum smaller than 43.
 

Constraints:

n == nums1.length == nums2.length
1 <= n <= 105
0 <= nums1[i], nums2[i] <= 105
0 <= k1, k2 <= 109






class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        from typing import List
        from collections import defaultdict
        import heapq   

        n = len(nums1)
        diff_count = defaultdict(int)
        
        # Calculate absolute differences and their counts
        for i in range(n):
            diff = abs(nums1[i] - nums2[i])
            diff_count[diff] += 1
        
        total_modifications = k1 + k2
        
        # Create a max-heap based on the differences
        max_heap = []
        for diff, count in diff_count.items():
            if diff > 0:
                heapq.heappush(max_heap, (-diff, count))  # Using negative for max-heap behavior

        while max_heap and total_modifications > 0:
            current_diff, count = heapq.heappop(max_heap)
            current_diff = -current_diff  # Convert back to positive
            
            if not max_heap:  # If this is the last element in the heap
                reduce_by = min(total_modifications, count)
                total_modifications -= reduce_by
                count -= reduce_by
                if current_diff - 1 > 0:  # Only push if the difference > 0
                    heapq.heappush(max_heap, (-(current_diff - 1), reduce_by))
                if count > 0:
                    heapq.heappush(max_heap, (-current_diff, count))
            else:
                reduce_by = min(total_modifications, count)
                total_modifications -= reduce_by
                count -= reduce_by
                if count > 0:
                    heapq.heappush(max_heap, (-current_diff, count))

                # Check if the next element in the heap has the difference `current_diff - 1`
                if max_heap and -max_heap[0][0] == current_diff - 1:
                    next_diff, next_count = heapq.heappop(max_heap)
                    next_diff = -next_diff
                    next_count += reduce_by
                    heapq.heappush(max_heap, (-next_diff, next_count))
                elif current_diff - 1 > 0:
                    heapq.heappush(max_heap, (-(current_diff - 1), reduce_by))

        # Calculate the final sum of squared differences
        result = 0
        while max_heap:
            diff, count = heapq.heappop(max_heap)
            result += (-diff) ** 2 * count
            
        return result
            