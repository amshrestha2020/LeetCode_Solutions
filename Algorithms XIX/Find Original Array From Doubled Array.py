An integer array original is transformed into a doubled array changed by appending twice the value of every element in original, and then randomly shuffling the resulting array.

Given an array changed, return original if changed is a doubled array. If changed is not a doubled array, return an empty array. The elements in original may be returned in any order.

 

Example 1:

Input: changed = [1,3,4,2,6,8]
Output: [1,3,4]
Explanation: One possible original array could be [1,3,4]:
- Twice the value of 1 is 1 * 2 = 2.
- Twice the value of 3 is 3 * 2 = 6.
- Twice the value of 4 is 4 * 2 = 8.
Other original arrays could be [4,3,1] or [3,1,4].
Example 2:

Input: changed = [6,3,0,1]
Output: []
Explanation: changed is not a doubled array.
Example 3:

Input: changed = [1]
Output: []
Explanation: changed is not a doubled array.
 

Constraints:

1 <= changed.length <= 105
0 <= changed[i] <= 105



class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        from collections import Counter
        from typing import List


        if len(changed) % 2 != 0:
            return []  # Must be even length to be a doubled array
        
        # Count the frequency of each number in the changed array
        count = Counter(changed)
        original = []
        
        # Process the number 0 first, as it needs special handling
        if count[0] % 2 != 0:
            return []  # If odd number of zeros, cannot form pairs
        original.extend([0] * (count[0] // 2))  # Add half the zeros to original
        
        # Remove the processed zeros from the count
        del count[0]
        
        # Process the other numbers in sorted order
        for x in sorted(count):
            if count[x] > 0:  # Only process if there are occurrences left
                if count[2 * x] < count[x]:
                    return []  # Not enough doubles for the originals
                
                # Add the original numbers to the result
                original.extend([x] * count[x])
                # Decrease the counts of doubles
                count[2 * x] -= count[x]
        
        return original