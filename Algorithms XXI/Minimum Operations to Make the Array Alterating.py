You are given a 0-indexed array nums consisting of n positive integers.

The array nums is called alternating if:

nums[i - 2] == nums[i], where 2 <= i <= n - 1.
nums[i - 1] != nums[i], where 1 <= i <= n - 1.
In one operation, you can choose an index i and change nums[i] into any positive integer.

Return the minimum number of operations required to make the array alternating.

 

Example 1:

Input: nums = [3,1,3,2,4,3]
Output: 3
Explanation:
One way to make the array alternating is by converting it to [3,1,3,1,3,1].
The number of operations required in this case is 3.
It can be proven that it is not possible to make the array alternating in less than 3 operations. 
Example 2:

Input: nums = [1,2,2,2,2]
Output: 2
Explanation:
One way to make the array alternating is by converting it to [1,2,1,2,1].
The number of operations required in this case is 2.
Note that the array cannot be converted to [2,2,2,2,2] because in this case nums[0] == nums[1] which violates the conditions of an alternating array.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 105





class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        from typing import List
        from collections import Counter


        even_count = Counter(nums[i] for i in range(0, len(nums), 2))
        odd_count = Counter(nums[i] for i in range(1, len(nums), 2))

        # Get the most common elements from both even and odd indices
        even_most_common = even_count.most_common(2)
        odd_most_common = odd_count.most_common(2)

        # Variables to store the top two candidates for even and odd indices
        even_first = even_most_common[0] if even_most_common else (None, 0)
        even_second = even_most_common[1] if len(even_most_common) > 1 else (None, 0)
        
        odd_first = odd_most_common[0] if odd_most_common else (None, 0)
        odd_second = odd_most_common[1] if len(odd_most_common) > 1 else (None, 0)

        # Calculate the number of operations needed
        if even_first[0] != odd_first[0]:
            # No conflict
            return (len(nums) // 2 - even_first[1]) + (len(nums) - len(nums) // 2 - odd_first[1])
        else:
            # Conflict: we have to choose between using the first or second most common
            return min(
                (len(nums) // 2 - even_first[1]) + (len(nums) - len(nums) // 2 - odd_second[1]),
                (len(nums) // 2 - even_second[1]) + (len(nums) - len(nums) // 2 - odd_first[1])
            )