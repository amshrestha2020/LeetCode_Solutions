You are given two arrays of integers nums1 and nums2, possibly of different lengths. The values in the arrays are between 1 and 6, inclusive.

In one operation, you can change any integer's value in any of the arrays to any value between 1 and 6, inclusive.

Return the minimum number of operations required to make the sum of values in nums1 equal to the sum of values in nums2. Return -1​​​​​ if it is not possible to make the sum of the two arrays equal.

 

Example 1:

Input: nums1 = [1,2,3,4,5,6], nums2 = [1,1,2,2,2,2]
Output: 3
Explanation: You can make the sums of nums1 and nums2 equal with 3 operations. All indices are 0-indexed.
- Change nums2[0] to 6. nums1 = [1,2,3,4,5,6], nums2 = [6,1,2,2,2,2].
- Change nums1[5] to 1. nums1 = [1,2,3,4,5,1], nums2 = [6,1,2,2,2,2].
- Change nums1[2] to 2. nums1 = [1,2,2,4,5,1], nums2 = [6,1,2,2,2,2].
Example 2:

Input: nums1 = [1,1,1,1,1,1,1], nums2 = [6]
Output: -1
Explanation: There is no way to decrease the sum of nums1 or to increase the sum of nums2 to make them equal.
Example 3:

Input: nums1 = [6,6], nums2 = [1]
Output: 3
Explanation: You can make the sums of nums1 and nums2 equal with 3 operations. All indices are 0-indexed. 
- Change nums1[0] to 2. nums1 = [2,6], nums2 = [1].
- Change nums1[1] to 2. nums1 = [2,2], nums2 = [1].
- Change nums2[0] to 4. nums1 = [2,2], nums2 = [4].
 

Constraints:

1 <= nums1.length, nums2.length <= 105
1 <= nums1[i], nums2[i] <= 6







class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        s1 = sum(nums1)
        s2 = sum(nums2)
        
        if s1 > s2:
            nums1, nums2 = nums2, nums1
            s1, s2 = s2, s1
        
        # Now s1 <= s2 and we need to cover the difference
        diff = s2 - s1
        if diff == 0:
            return 0

        # Array to keep track of the number of possible operations by their impact
        counts = [0] * 6  # counts[i] will store the number of changes giving i impact
        
        # Calculate impacts for increasing nums1 elements to 6
        for x in nums1:
            counts[6 - x] += 1
        
        # Calculate impacts for decreasing nums2 elements to 1
        for x in nums2:
            counts[x - 1] += 1

        # Process impacts to minimize the number of operations
        ans = 0
        for i in range(5, 0, -1):
            while counts[i] > 0 and diff > 0:
                diff -= i
                counts[i] -= 1
                ans += 1
                if diff <= 0:
                    return ans
        
        return -1