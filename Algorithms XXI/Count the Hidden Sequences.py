You are given a 0-indexed array of n integers differences, which describes the differences between each pair of consecutive integers of a hidden sequence of length (n + 1). More formally, call the hidden sequence hidden, then we have that differences[i] = hidden[i + 1] - hidden[i].

You are further given two integers lower and upper that describe the inclusive range of values [lower, upper] that the hidden sequence can contain.

For example, given differences = [1, -3, 4], lower = 1, upper = 6, the hidden sequence is a sequence of length 4 whose elements are in between 1 and 6 (inclusive).
[3, 4, 1, 5] and [4, 5, 2, 6] are possible hidden sequences.
[5, 6, 3, 7] is not possible since it contains an element greater than 6.
[1, 2, 3, 4] is not possible since the differences are not correct.
Return the number of possible hidden sequences there are. If there are no possible sequences, return 0.

 

Example 1:

Input: differences = [1,-3,4], lower = 1, upper = 6
Output: 2
Explanation: The possible hidden sequences are:
- [3, 4, 1, 5]
- [4, 5, 2, 6]
Thus, we return 2.
Example 2:

Input: differences = [3,-4,5,1,-2], lower = -4, upper = 5
Output: 4
Explanation: The possible hidden sequences are:
- [-3, 0, -4, 1, 2, 0]
- [-2, 1, -3, 2, 3, 1]
- [-1, 2, -2, 3, 4, 2]
- [0, 3, -1, 4, 5, 3]
Thus, we return 4.
Example 3:

Input: differences = [4,-7,2], lower = 3, upper = 6
Output: 0
Explanation: There are no possible hidden sequences. Thus, we return 0.
 

Constraints:

n == differences.length
1 <= n <= 105
-105 <= differences[i] <= 105
-105 <= lower <= upper <= 105




class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        from typing import List


        min_value = 0
        max_value = 0
        current_sum = 0
        
        # Calculate the minimum and maximum values that hidden[0] can take
        for diff in differences:
            current_sum += diff
            min_value = min(min_value, current_sum)  # Track the minimum cumulative sum
            max_value = max(max_value, current_sum)  # Track the maximum cumulative sum
            
        # Calculate the range for hidden[0]
        valid_start_min = lower - min_value  # The minimum value that hidden[0] can take
        valid_start_max = upper - max_value  # The maximum value that hidden[0] can take
        
        # Calculate the number of valid integers for hidden[0] within the range
        return max(0, valid_start_max - valid_start_min + 1)