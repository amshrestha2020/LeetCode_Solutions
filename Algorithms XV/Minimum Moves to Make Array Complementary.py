You are given an integer array nums of even length n and an integer limit. In one move, you can replace any integer from nums with another integer between 1 and limit, inclusive.

The array nums is complementary if for all indices i (0-indexed), nums[i] + nums[n - 1 - i] equals the same number. For example, the array [1,2,3,4] is complementary because for all indices i, nums[i] + nums[n - 1 - i] = 5.

Return the minimum number of moves required to make nums complementary.

 

Example 1:

Input: nums = [1,2,4,3], limit = 4
Output: 1
Explanation: In 1 move, you can change nums to [1,2,2,3] (underlined elements are changed).
nums[0] + nums[3] = 1 + 3 = 4.
nums[1] + nums[2] = 2 + 2 = 4.
nums[2] + nums[1] = 2 + 2 = 4.
nums[3] + nums[0] = 3 + 1 = 4.
Therefore, nums[i] + nums[n-1-i] = 4 for every i, so nums is complementary.
Example 2:

Input: nums = [1,2,2,1], limit = 2
Output: 2
Explanation: In 2 moves, you can change nums to [2,2,2,2]. You cannot change any number to 3 since 3 > limit.
Example 3:

Input: nums = [1,2,1,2], limit = 2
Output: 0
Explanation: nums is already complementary.
 

Constraints:

n == nums.length
2 <= n <= 105
1 <= nums[i] <= limit <= 105
n is even.


class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        delta = [0] * (2 * limit + 2)  # A delta array to track changes
        
        for i in range(n // 2):
            a, b = nums[i], nums[n - 1 - i]
            
            # Minimum and maximum possible sums for this pair
            min_sum = min(a, b) + 1
            max_sum = max(a, b) + limit
            
            # For sum = a + b, no move is needed
            target_sum = a + b
            
            # Update the delta array based on the needed operations
            delta[2] += 2  # Assume 2 moves for any sum initially
            delta[min_sum] -= 1  # 1 move if sum is between min_sum and max_sum
            delta[target_sum] -= 1  # No move for target_sum
            delta[target_sum + 1] += 1  # 1 move again after the target_sum
            delta[max_sum + 1] += 1  # Restore the 2 move assumption after max_sum
        
        # Now calculate the minimum moves based on delta
        moves = 0
        result = float('inf')
        
        for x in range(2, 2 * limit + 1):
            moves += delta[x]  # Increment moves by the change in delta
            result = min(result, moves)  # Track the minimum moves required
        
        return result        
