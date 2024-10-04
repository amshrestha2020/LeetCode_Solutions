Design a data structure to find the frequency of a given value in a given subarray.

The frequency of a value in a subarray is the number of occurrences of that value in the subarray.

Implement the RangeFreqQuery class:

RangeFreqQuery(int[] arr) Constructs an instance of the class with the given 0-indexed integer array arr.
int query(int left, int right, int value) Returns the frequency of value in the subarray arr[left...right].
A subarray is a contiguous sequence of elements within an array. arr[left...right] denotes the subarray that contains the elements of nums between indices left and right (inclusive).

 

Example 1:

Input
["RangeFreqQuery", "query", "query"]
[[[12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]], [1, 2, 4], [0, 11, 33]]
Output
[null, 1, 2]

Explanation
RangeFreqQuery rangeFreqQuery = new RangeFreqQuery([12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]);
rangeFreqQuery.query(1, 2, 4); // return 1. The value 4 occurs 1 time in the subarray [33, 4]
rangeFreqQuery.query(0, 11, 33); // return 2. The value 33 occurs 2 times in the whole array.
 

Constraints:

1 <= arr.length <= 105
1 <= arr[i], value <= 104
0 <= left <= right < arr.length
At most 105 calls will be made to query




class RangeFreqQuery:
    from collections import defaultdict
    from bisect import bisect_left, bisect_right

    def __init__(self, arr: List[int]):
        self.indices_map = defaultdict(list)
        
        # Populate the map with indices for each value
        for i, num in enumerate(arr):
            self.indices_map[num].append(i)        

    def query(self, left: int, right: int, value: int) -> int:
        if value not in self.indices_map:
            return 0
        
        # Get the list of indices where the value occurs
        indices = self.indices_map[value]
        
        # Use binary search to find the valid range of indices within [left, right]
        left_idx = bisect_left(indices, left)   # first index >= left
        right_idx = bisect_right(indices, right)  # first index > right
        
        # The count of occurrences is the number of indices between left_idx and right_idx
        return right_idx - left_idx        


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)