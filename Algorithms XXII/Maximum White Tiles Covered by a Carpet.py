You are given a 2D integer array tiles where tiles[i] = [li, ri] represents that every tile j in the range li <= j <= ri is colored white.

You are also given an integer carpetLen, the length of a single carpet that can be placed anywhere.

Return the maximum number of white tiles that can be covered by the carpet.

 

Example 1:


Input: tiles = [[1,5],[10,11],[12,18],[20,25],[30,32]], carpetLen = 10
Output: 9
Explanation: Place the carpet starting on tile 10. 
It covers 9 white tiles, so we return 9.
Note that there may be other places where the carpet covers 9 white tiles.
It can be shown that the carpet cannot cover more than 9 white tiles.
Example 2:


Input: tiles = [[10,11],[1,1]], carpetLen = 2
Output: 2
Explanation: Place the carpet starting on tile 10. 
It covers 2 white tiles, so we return 2.
 

Constraints:

1 <= tiles.length <= 5 * 104
tiles[i].length == 2
1 <= li <= ri <= 109
1 <= carpetLen <= 109
The tiles are non-overlapping.



class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        from typing import List


        sorted_tiles = sorted(tiles, key=lambda x: x[0])
        res = 0  # To store the maximum covered tiles
        total = 0  # To store the total length of tiles covered
        right = 0  # Pointer to the rightmost tile being considered

        # Step 2: Iterate through each tile
        for tile in sorted_tiles:
            start = tile[0]
            end = start + carpetLen - 1  # Calculate the end position of the carpet
            
            # Step 3: Move the right pointer to count total covered tiles
            while right < len(sorted_tiles) and sorted_tiles[right][1] < end:
                total += sorted_tiles[right][1] - sorted_tiles[right][0] + 1
                right += 1
            
            # Step 4: Check if we can fully cover the next tile
            if right == len(sorted_tiles) or sorted_tiles[right][0] > end:
                res = max(res, total)  # Update result if no tile overlaps
            else:
                # Add the covered length of the partially covered tile
                res = max(res, total + (end - sorted_tiles[right][0] + 1))
            
            # Step 5: Remove the current tile from the total count
            total -= tile[1] - tile[0] + 1
        
        return res         