Given two integers tomatoSlices and cheeseSlices. The ingredients of different burgers are as follows:

Jumbo Burger: 4 tomato slices and 1 cheese slice.
Small Burger: 2 Tomato slices and 1 cheese slice.
Return [total_jumbo, total_small] so that the number of remaining tomatoSlices equal to 0 and the number of remaining cheeseSlices equal to 0. If it is not possible to make the remaining tomatoSlices and cheeseSlices equal to 0 return [].

 

Example 1:

Input: tomatoSlices = 16, cheeseSlices = 7
Output: [1,6]
Explantion: To make one jumbo burger and 6 small burgers we need 4*1 + 2*6 = 16 tomato and 1 + 6 = 7 cheese.
There will be no remaining ingredients.
Example 2:

Input: tomatoSlices = 17, cheeseSlices = 4
Output: []
Explantion: There will be no way to use all ingredients to make small and jumbo burgers.
Example 3:

Input: tomatoSlices = 4, cheeseSlices = 17
Output: []
Explantion: Making 1 jumbo burger there will be 16 cheese remaining and making 2 small burgers there will be 15 cheese remaining.
 

Constraints:

0 <= tomatoSlices, cheeseSlices <= 107





from typing import List

class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        # Check if it's possible to find a valid solution
        if tomatoSlices < 2 * cheeseSlices or (tomatoSlices - 2 * cheeseSlices) % 2 != 0:
            return []
        
        # Calculate number of jumbo burgers
        j = (tomatoSlices - 2 * cheeseSlices) // 2
        
        # Calculate number of small burgers
        s = cheeseSlices - j
        
        # Check if the solution is valid
        if j < 0 or s < 0:
            return []
        
        return [j, s]

# Example usage:
sol = Solution()
print(sol.numOfBurgers(16, 7))  # Output: [1, 6]
print(sol.numOfBurgers(17, 4))  # Output: []
print(sol.numOfBurgers(4, 17))  # Output: []
