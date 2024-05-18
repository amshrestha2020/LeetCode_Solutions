You are stacking blocks to form a pyramid. Each block has a color, which is represented by a single letter. Each row of blocks contains one less block than the row beneath it and is centered on top.

To make the pyramid aesthetically pleasing, there are only specific triangular patterns that are allowed. A triangular pattern consists of a single block stacked on top of two blocks. The patterns are given as a list of three-letter strings allowed, where the first two characters of a pattern represent the left and right bottom blocks respectively, and the third character is the top block.

For example, "ABC" represents a triangular pattern with a 'C' block stacked on top of an 'A' (left) and 'B' (right) block. Note that this is different from "BAC" where 'B' is on the left bottom and 'A' is on the right bottom.
You start with a bottom row of blocks bottom, given as a single string, that you must use as the base of the pyramid.

Given bottom and allowed, return true if you can build the pyramid all the way to the top such that every triangular pattern in the pyramid is in allowed, or false otherwise.

 

Example 1:


Input: bottom = "BCD", allowed = ["BCC","CDE","CEA","FFF"]
Output: true
Explanation: The allowed triangular patterns are shown on the right.
Starting from the bottom (level 3), we can build "CE" on level 2 and then build "A" on level 1.
There are three triangular patterns in the pyramid, which are "BCC", "CDE", and "CEA". All are allowed.
Example 2:


Input: bottom = "AAAA", allowed = ["AAB","AAC","BCD","BBE","DEF"]
Output: false
Explanation: The allowed triangular patterns are shown on the right.
Starting from the bottom (level 4), there are multiple ways to build level 3, but trying all the possibilites, you will get always stuck before building level 1.
 

Constraints:

2 <= bottom.length <= 6
0 <= allowed.length <= 216
allowed[i].length == 3
The letters in all input strings are from the set {'A', 'B', 'C', 'D', 'E', 'F'}.
All the values of allowed are unique.




from collections import defaultdict
from typing import List

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        # Preprocess the allowed patterns into a dictionary
        patterns = defaultdict(list)
        for pattern in allowed:
            patterns[pattern[:2]].append(pattern[2])
        
        # Helper function to check if the pyramid can be built
        def can_build(current):
            if len(current) == 1:
                return True
            next_row = []
            return build_next_row(current, 0, next_row)
        
        # Recursive function to build the next row
        def build_next_row(current, index, next_row):
            if index == len(current) - 1:
                return can_build("".join(next_row))
            
            base = current[index:index+2]
            if base not in patterns:
                return False
            
            for top in patterns[base]:
                next_row.append(top)
                if build_next_row(current, index + 1, next_row):
                    return True
                next_row.pop()
            
            return False
        
        return can_build(bottom)

# Example usage:
solution = Solution()
print(solution.pyramidTransition("BCD", ["BCC","CDE","CEA","FFF"]))  # Output: True
print(solution.pyramidTransition("AAAA", ["AAB","AAC","BCD","BBE","DEF"]))  # Output: False
