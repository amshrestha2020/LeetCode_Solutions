Design a data structure that efficiently finds the majority element of a given subarray.

The majority element of a subarray is an element that occurs threshold times or more in the subarray.

Implementing the MajorityChecker class:

MajorityChecker(int[] arr) Initializes the instance of the class with the given array arr.
int query(int left, int right, int threshold) returns the element in the subarray arr[left...right] that occurs at least threshold times, or -1 if no such element exists.
 

Example 1:

Input
["MajorityChecker", "query", "query", "query"]
[[[1, 1, 2, 2, 1, 1]], [0, 5, 4], [0, 3, 3], [2, 3, 2]]
Output
[null, 1, -1, 2]

Explanation
MajorityChecker majorityChecker = new MajorityChecker([1, 1, 2, 2, 1, 1]);
majorityChecker.query(0, 5, 4); // return 1
majorityChecker.query(0, 3, 3); // return -1
majorityChecker.query(2, 3, 2); // return 2
 

Constraints:

1 <= arr.length <= 2 * 104
1 <= arr[i] <= 2 * 104
0 <= left <= right < arr.length
threshold <= right - left + 1
2 * threshold > right - left + 1
At most 104 calls will be made to query




from collections import defaultdict
from bisect import bisect_left, bisect_right
from typing import List

class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.arr = arr
        self.pos = defaultdict(list)
        for i, num in enumerate(arr):
            self.pos[num].append(i)
        self.segment_tree = [None] * (4 * len(arr))
        self.build_segment_tree(0, 0, len(arr) - 1)
    
    def build_segment_tree(self, node, start, end):
        if start == end:
            self.segment_tree[node] = self.arr[start]
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            self.build_segment_tree(left_child, start, mid)
            self.build_segment_tree(right_child, mid + 1, end)
            left_majority = self.segment_tree[left_child]
            right_majority = self.segment_tree[right_child]
            if left_majority is not None and self.count_range(start, end, left_majority) > (end - start + 1) // 2:
                self.segment_tree[node] = left_majority
            elif right_majority is not None and self.count_range(start, end, right_majority) > (end - start + 1) // 2:
                self.segment_tree[node] = right_majority
            else:
                self.segment_tree[node] = None

    def count_range(self, left, right, x):
        if x not in self.pos:
            return 0
        positions = self.pos[x]
        left_index = bisect_left(positions, left)
        right_index = bisect_right(positions, right) - 1
        return max(0, right_index - left_index + 1)
    
    def query(self, left: int, right: int, threshold: int) -> int:
        candidate = self.query_segment_tree(0, 0, len(self.arr) - 1, left, right)
        if candidate is not None and self.count_range(left, right, candidate) >= threshold:
            return candidate
        return -1
    
    def query_segment_tree(self, node, start, end, left, right):
        if right < start or end < left:
            return None
        if left <= start and end <= right:
            return self.segment_tree[node]
        mid = (start + end) // 2
        left_majority = self.query_segment_tree(2 * node + 1, start, mid, left, right)
        right_majority = self.query_segment_tree(2 * node + 2, mid + 1, end, left, right)
        if left_majority is not None and self.count_range(left, right, left_majority) > (right - left + 1) // 2:
            return left_majority
        if right_majority is not None and self.count_range(left, right, right_majority) > (right - left + 1) // 2:
            return right_majority
        return None

# Example usage:
majorityChecker = MajorityChecker([1, 1, 2, 2, 1, 1])
print(majorityChecker.query(0, 5, 4))  # return 1
print(majorityChecker.query(0, 3, 3))  # return -1
print(majorityChecker.query(2, 3, 2))  # return 2


# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)