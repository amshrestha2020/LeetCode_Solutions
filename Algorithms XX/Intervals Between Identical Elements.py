You are given a 0-indexed array of n integers arr.

The interval between two elements in arr is defined as the absolute difference between their indices. More formally, the interval between arr[i] and arr[j] is |i - j|.

Return an array intervals of length n where intervals[i] is the sum of intervals between arr[i] and each element in arr with the same value as arr[i].

Note: |x| is the absolute value of x.

 

Example 1:

Input: arr = [2,1,3,1,2,3,3]
Output: [4,2,7,2,4,4,5]
Explanation:
- Index 0: Another 2 is found at index 4. |0 - 4| = 4
- Index 1: Another 1 is found at index 3. |1 - 3| = 2
- Index 2: Two more 3s are found at indices 5 and 6. |2 - 5| + |2 - 6| = 7
- Index 3: Another 1 is found at index 1. |3 - 1| = 2
- Index 4: Another 2 is found at index 0. |4 - 0| = 4
- Index 5: Two more 3s are found at indices 2 and 6. |5 - 2| + |5 - 6| = 4
- Index 6: Two more 3s are found at indices 2 and 5. |6 - 2| + |6 - 5| = 5
Example 2:

Input: arr = [10,5,10,10]
Output: [5,0,3,4]
Explanation:
- Index 0: Two more 10s are found at indices 2 and 3. |0 - 2| + |0 - 3| = 5
- Index 1: There is only one 5 in the array, so its sum of intervals to identical elements is 0.
- Index 2: Two more 10s are found at indices 0 and 3. |2 - 0| + |2 - 3| = 3
- Index 3: Two more 10s are found at indices 0 and 2. |3 - 0| + |3 - 2| = 4
 

Constraints:

n == arr.length
1 <= n <= 105
1 <= arr[i] <= 105
 


class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        from collections import defaultdict
        from typing import List


        n = len(arr)
        intervals = [0] * n
        
        # Step 1: Group indices by value
        index_map = defaultdict(list)
        for index, value in enumerate(arr):
            index_map[value].append(index)
        
        # Step 2: Calculate sum of intervals for each group
        for indices in index_map.values():
            k = len(indices)
            if k < 2:
                continue  # No intervals to calculate if there's only one index
            
            prefix_sum = [0] * (k + 1)
            
            # Calculate prefix sums of indices
            for i in range(k):
                prefix_sum[i + 1] = prefix_sum[i] + indices[i]
            
            # Calculate intervals for each index in the current group
            for i in range(k):
                current_index = indices[i]
                
                # Calculate the distance for all previous indices
                sum_left = current_index * i - prefix_sum[i]
                
                # Calculate the distance for all next indices
                sum_right = prefix_sum[k] - prefix_sum[i + 1] - current_index * (k - 1 - i)
                
                # Total interval sum for this index
                intervals[current_index] += sum_left + sum_right
        
        return intervals