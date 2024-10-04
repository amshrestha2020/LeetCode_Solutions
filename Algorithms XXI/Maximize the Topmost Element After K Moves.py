You are given a 0-indexed integer array nums representing the contents of a pile, where nums[0] is the topmost element of the pile.

In one move, you can perform either of the following:

If the pile is not empty, remove the topmost element of the pile.
If there are one or more removed elements, add any one of them back onto the pile. This element becomes the new topmost element.
You are also given an integer k, which denotes the total number of moves to be made.

Return the maximum value of the topmost element of the pile possible after exactly k moves. In case it is not possible to obtain a non-empty pile after k moves, return -1.

 

Example 1:

Input: nums = [5,2,2,4,0,6], k = 4
Output: 5
Explanation:
One of the ways we can end with 5 at the top of the pile after 4 moves is as follows:
- Step 1: Remove the topmost element = 5. The pile becomes [2,2,4,0,6].
- Step 2: Remove the topmost element = 2. The pile becomes [2,4,0,6].
- Step 3: Remove the topmost element = 2. The pile becomes [4,0,6].
- Step 4: Add 5 back onto the pile. The pile becomes [5,4,0,6].
Note that this is not the only way to end with 5 at the top of the pile. It can be shown that 5 is the largest answer possible after 4 moves.
Example 2:

Input: nums = [2], k = 1
Output: -1
Explanation: 
In the first move, our only option is to pop the topmost element of the pile.
Since it is not possible to obtain a non-empty pile after one move, we return -1.
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i], k <= 109



class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:

        def max_array(arr):
            """Helper function to find the maximum value in the array."""
            m = float('-inf')  # Use negative infinity as the initial maximum
            for num in arr:
                if num > m:
                    m = num
            return m

        len_nums = len(nums)

        # Case 1: When k > len
        if k > len_nums:
            if len_nums == 1:
                if k % 2 != 0:  # If k is odd and there's only one element
                    return -1
            return max_array(nums)  # Return the maximum element

        # Case 2: When k == len
        elif k == len_nums:
            temp = nums[:k - 1]  # Slice to get the first k-1 elements
            if temp:
                return max_array(temp)

        # Case 3: When k < len
        else:
            if k == 0:
                return nums[0]  # If k is zero, return the top element
            else:
                temp = nums[:k - 1]  # Slice to get the first k-1 elements
                m = max_array(temp)
                return max(m, nums[k])  # Return the maximum of m and nums[k]

        return -1