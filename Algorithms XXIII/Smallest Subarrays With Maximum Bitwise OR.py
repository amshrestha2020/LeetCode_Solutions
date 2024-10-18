You are given a 0-indexed array nums of length n, consisting of non-negative integers. For each index i from 0 to n - 1, you must determine the size of the minimum sized non-empty subarray of nums starting at i (inclusive) that has the maximum possible bitwise OR.

In other words, let Bij be the bitwise OR of the subarray nums[i...j]. You need to find the smallest subarray starting at i, such that bitwise OR of this subarray is equal to max(Bik) where i <= k <= n - 1.
The bitwise OR of an array is the bitwise OR of all the numbers in it.

Return an integer array answer of size n where answer[i] is the length of the minimum sized subarray starting at i with maximum bitwise OR.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,0,2,1,3]
Output: [3,3,2,2,1]
Explanation:
The maximum possible bitwise OR starting at any index is 3. 
- Starting at index 0, the shortest subarray that yields it is [1,0,2].
- Starting at index 1, the shortest subarray that yields the maximum bitwise OR is [0,2,1].
- Starting at index 2, the shortest subarray that yields the maximum bitwise OR is [2,1].
- Starting at index 3, the shortest subarray that yields the maximum bitwise OR is [1,3].
- Starting at index 4, the shortest subarray that yields the maximum bitwise OR is [3].
Therefore, we return [3,3,2,2,1]. 
Example 2:

Input: nums = [1,2]
Output: [2,1]
Explanation:
Starting at index 0, the shortest subarray that yields the maximum bitwise OR is of length 2.
Starting at index 1, the shortest subarray that yields the maximum bitwise OR is of length 1.
Therefore, we return [2,1].
 

Constraints:

n == nums.length
1 <= n <= 105
0 <= nums[i] <= 109



class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        from typing import List

        bit_positions = [0] * 32
        # Array to store the result
        ans = [0] * len(nums)

        # Iterate through nums from the end to the beginning
        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            # Update the last seen position of each bit
            for j in range(32):
                mask = 1 << j
                if (num & mask) > 0:
                    bit_positions[j] = i
            
            # Find the maximum index of the last seen bits
            max_pos = i
            for e in bit_positions:
                max_pos = max(e, max_pos)

            # Calculate the size of the smallest subarray
            ans[i] = max_pos - i + 1

        return ans
    
    