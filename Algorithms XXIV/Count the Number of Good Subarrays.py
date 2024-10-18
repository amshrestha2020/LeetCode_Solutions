Given an integer array nums and an integer k, return the number of good subarrays of nums.

A subarray arr is good if it there are at least k pairs of indices (i, j) such that i < j and arr[i] == arr[j].

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1,1,1], k = 10
Output: 1
Explanation: The only good subarray is the array nums itself.
Example 2:

Input: nums = [3,1,4,3,2,2,4], k = 2
Output: 4
Explanation: There are 4 different good subarrays:
- [3,1,4,3,2,2] that has 2 pairs.
- [3,1,4,3,2,2,4] that has 3 pairs.
- [1,4,3,2,2,4] that has 2 pairs.
- [4,3,2,2,4] that has 2 pairs.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i], k <= 109



class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        from typing import List
        from collections import defaultdict        

        freq = defaultdict(int)
        left = 0
        count = 0
        pairs = 0
        
        for right in range(len(nums)):
            # Add the current number to the frequency map
            freq[nums[right]] += 1
            # Update the number of pairs
            pairs += freq[nums[right]] - 1  # pairs are formed by the new occurrence
            
            # While we have at least k pairs, move the left pointer
            while pairs >= k:
                # Count the number of valid subarrays starting from left
                count += len(nums) - right  # All subarrays from left to the end
                # Remove the leftmost element from the frequency map
                pairs -= freq[nums[left]] - 1  # Remove pairs formed by the leftmost occurrence
                freq[nums[left]] -= 1
                # If frequency becomes zero, we remove the element from the map
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1
        
        return count