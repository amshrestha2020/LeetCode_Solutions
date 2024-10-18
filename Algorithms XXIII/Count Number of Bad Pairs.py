You are given a 0-indexed integer array nums. A pair of indices (i, j) is a bad pair if i < j and j - i != nums[j] - nums[i].

Return the total number of bad pairs in nums.

 

Example 1:

Input: nums = [4,1,3,3]
Output: 5
Explanation: The pair (0, 1) is a bad pair since 1 - 0 != 1 - 4.
The pair (0, 2) is a bad pair since 2 - 0 != 3 - 4, 2 != -1.
The pair (0, 3) is a bad pair since 3 - 0 != 3 - 4, 3 != -1.
The pair (1, 2) is a bad pair since 2 - 1 != 3 - 1, 1 != 2.
The pair (2, 3) is a bad pair since 3 - 2 != 3 - 3, 1 != 0.
There are a total of 5 bad pairs, so we return 5.
Example 2:

Input: nums = [1,2,3,4,5]
Output: 0
Explanation: There are no bad pairs.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109




class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        freq_map = {}
        good_pairs = 0
        
        for i in range(n):
            diff = nums[i] - i
            if diff in freq_map:
                good_pairs += freq_map[diff]  # Count good pairs with this difference
            # Update the frequency of this difference
            if diff in freq_map:
                freq_map[diff] += 1
            else:
                freq_map[diff] = 1
        
        # Total pairs is n * (n - 1) // 2
        total_pairs = n * (n - 1) // 2
        bad_pairs = total_pairs - good_pairs
        
        return bad_pairs        