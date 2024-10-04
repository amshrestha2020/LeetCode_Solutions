You are given an integer array nums and an integer k. Append k unique positive integers that do not appear in nums to nums such that the resulting total sum is minimum.

Return the sum of the k integers appended to nums.

 

Example 1:

Input: nums = [1,4,25,10,25], k = 2
Output: 5
Explanation: The two unique positive integers that do not appear in nums which we append are 2 and 3.
The resulting sum of nums is 1 + 4 + 25 + 10 + 25 + 2 + 3 = 70, which is the minimum.
The sum of the two integers appended is 2 + 3 = 5, so we return 5.
Example 2:

Input: nums = [5,6], k = 6
Output: 25
Explanation: The six unique positive integers that do not appear in nums which we append are 1, 2, 3, 4, 7, and 8.
The resulting sum of nums is 5 + 6 + 1 + 2 + 3 + 4 + 7 + 8 = 36, which is the minimum. 
The sum of the six integers appended is 1 + 2 + 3 + 4 + 7 + 8 = 25, so we return 25.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= k <= 108


class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums = sorted(set(nums))
        
        current = 1
        total_sum = 0
        i = 0
        n = len(nums)
        
        # Step 2: Iterate through nums and append missing numbers until k becomes 0
        while k > 0 and i < n:
            # Add numbers between 'current' and nums[i] that are missing
            if current < nums[i]:
                # How many numbers we can append from current to nums[i] - 1
                count = min(k, nums[i] - current)
                total_sum += (current + current + count - 1) * count // 2  # Sum of first `count` integers
                k -= count
            # Move current to nums[i] + 1
            current = nums[i] + 1
            i += 1
        
        # Step 3: If we still need more numbers after the loop
        if k > 0:
            total_sum += (current + current + k - 1) * k // 2
        
        return total_sum        