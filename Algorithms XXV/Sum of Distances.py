You are given a 0-indexed integer array nums. There exists an array arr of length nums.length, where arr[i] is the sum of |i - j| over all j such that nums[j] == nums[i] and j != i. If there is no such j, set arr[i] to be 0.

Return the array arr.

 

Example 1:

Input: nums = [1,3,1,1,2]
Output: [5,0,3,4,0]
Explanation: 
When i = 0, nums[0] == nums[2] and nums[0] == nums[3]. Therefore, arr[0] = |0 - 2| + |0 - 3| = 5. 
When i = 1, arr[1] = 0 because there is no other index with value 3.
When i = 2, nums[2] == nums[0] and nums[2] == nums[3]. Therefore, arr[2] = |2 - 0| + |2 - 3| = 3. 
When i = 3, nums[3] == nums[0] and nums[3] == nums[2]. Therefore, arr[3] = |3 - 0| + |3 - 2| = 4. 
When i = 4, arr[4] = 0 because there is no other index with value 2. 

Example 2:

Input: nums = [0,5,3]
Output: [0,0,0]
Explanation: Since each element in nums is distinct, arr[i] = 0 for all i.
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109
 

Note: This question is the same as 2121: Intervals Between Identical Elements.


class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        from typing import List
        from collections import defaultdict

        index_map = defaultdict(list)
        
        # Populate the index_map with indices of each number
        for i, num in enumerate(nums):
            index_map[num].append(i)
        
        # Initialize the result array
        result = [0] * len(nums)
        
        # Calculate distances for each unique number's indices
        for indices in index_map.values():
            if len(indices) > 1:
                total_distance = 0
                n = len(indices)
                
                # Precompute the prefix sum to help in calculating distances efficiently
                prefix_sum = [0] * (n + 1)
                for i in range(n):
                    prefix_sum[i + 1] = prefix_sum[i] + indices[i]
                
                # Calculate the distance for each index in the group
                for i in range(n):
                    # The current index in the original array
                    current_index = indices[i]
                    
                    # Calculate the distance contributed by all other indices
                    left_contribution = current_index * i - prefix_sum[i]  # Contribution from the left
                    right_contribution = prefix_sum[n] - prefix_sum[i + 1] - current_index * (n - i - 1)  # Contribution from the right
                    
                    result[current_index] = left_contribution + right_contribution
        
        return result