In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a move consists of either replacing one occurrence of "XL" with "LX", or replacing one occurrence of "RX" with "XR". Given the starting string start and the ending string end, return True if and only if there exists a sequence of moves to transform one string to the other.

 

Example 1:

Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
Output: true
Explanation: We can transform start to end following these steps:
RXXLRXRXL ->
XRXLRXRXL ->
XRLXRXRXL ->
XRLXXRRXL ->
XRLXXRRLX
Example 2:

Input: start = "X", end = "L"
Output: false
 

Constraints:

1 <= start.length <= 104
start.length == end.length
Both start and end will only consist of characters in 'L', 'R', and 'X'.





class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        i, j, len_s, len_e = 0, 0, len(start), len(end)
        while i < len_s and j < len_e:
            # Skip all 'X' in both strings.
            while i < len_s and start[i] == 'X':
                i += 1
            while j < len_e and end[j] == 'X':
                j += 1

            # If both pointers have reached the end, return True.
            if i == len_s and j == len_e:
                return True

            # If only one pointer has reached the end, return False.
            if (i == len_s) != (j == len_e):
                return False

            # If the characters at both pointers are not equal, return False.
            if start[i] != end[j]:
                return False

            # If the character at the current pointer is 'L', then the index in 'start' should not be less than the index in 'end'.
            if start[i] == 'L' and i < j:
                return False

            # If the character at the current pointer is 'R', then the index in 'start' should not be greater than the index in 'end'.
            if start[i] == 'R' and i > j:
                return False

            i += 1
            j += 1

        # Skip all 'X' in both strings.
        while i < len_s and start[i] == 'X':
            i += 1
        while j < len_e and end[j] == 'X':
            j += 1

        # If both pointers have reached the end, return True. Otherwise, return False.
        return i == len_s and j == len_e
