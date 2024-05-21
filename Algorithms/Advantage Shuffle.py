You are given two integer arrays nums1 and nums2 both of the same length. The advantage of nums1 with respect to nums2 is the number of indices i for which nums1[i] > nums2[i].

Return any permutation of nums1 that maximizes its advantage with respect to nums2.

 

Example 1:

Input: nums1 = [2,7,11,15], nums2 = [1,10,4,11]
Output: [2,11,7,15]
Example 2:

Input: nums1 = [12,24,8,32], nums2 = [13,25,32,11]
Output: [24,32,8,12]
 

Constraints:

1 <= nums1.length <= 105
nums2.length == nums1.length
0 <= nums1[i], nums2[i] <= 109





class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        sorted_nums1 = sorted(nums1)
        sorted_nums2 = sorted((num, i) for i, num in enumerate(nums2))
        assigned = {i: [] for i in range(len(nums1))}
        remaining = []
        j = 0
        for num in sorted_nums1:
            if num > sorted_nums2[j][0]:
                assigned[sorted_nums2[j][1]].append(num)
                j += 1
            else:
                remaining.append(num)
        for i in range(len(nums1)):
            if not assigned[i]:
                assigned[i].append(remaining.pop())
        return [assigned[i][0] for i in range(len(nums1))]
