Alice and Bob are opponents in an archery competition. The competition has set the following rules:

Alice first shoots numArrows arrows and then Bob shoots numArrows arrows.
The points are then calculated as follows:
The target has integer scoring sections ranging from 0 to 11 inclusive.
For each section of the target with score k (in between 0 to 11), say Alice and Bob have shot ak and bk arrows on that section respectively. If ak >= bk, then Alice takes k points. If ak < bk, then Bob takes k points.
However, if ak == bk == 0, then nobody takes k points.
For example, if Alice and Bob both shot 2 arrows on the section with score 11, then Alice takes 11 points. On the other hand, if Alice shot 0 arrows on the section with score 11 and Bob shot 2 arrows on that same section, then Bob takes 11 points.

You are given the integer numArrows and an integer array aliceArrows of size 12, which represents the number of arrows Alice shot on each scoring section from 0 to 11. Now, Bob wants to maximize the total number of points he can obtain.

Return the array bobArrows which represents the number of arrows Bob shot on each scoring section from 0 to 11. The sum of the values in bobArrows should equal numArrows.

If there are multiple ways for Bob to earn the maximum total points, return any one of them.

 

Example 1:


Input: numArrows = 9, aliceArrows = [1,1,0,1,0,0,2,1,0,1,2,0]
Output: [0,0,0,0,1,1,0,0,1,2,3,1]
Explanation: The table above shows how the competition is scored. 
Bob earns a total point of 4 + 5 + 8 + 9 + 10 + 11 = 47.
It can be shown that Bob cannot obtain a score higher than 47 points.
Example 2:


Input: numArrows = 3, aliceArrows = [0,0,1,0,0,0,0,0,0,0,0,2]
Output: [0,0,0,0,0,0,0,0,1,1,1,0]
Explanation: The table above shows how the competition is scored.
Bob earns a total point of 8 + 9 + 10 = 27.
It can be shown that Bob cannot obtain a score higher than 27 points.
 

Constraints:

1 <= numArrows <= 105
aliceArrows.length == bobArrows.length == 12
0 <= aliceArrows[i], bobArrows[i] <= numArrows
sum(aliceArrows[i]) == numArrows


class Solution:
    def helper(self, numArrows: int, aliceArrows: List[int], bobArrows: List[int], index: int, maxScore: int, soFarSum: int, soFar: List[int]) -> None:
        from typing import List


        if numArrows == 0 or index == len(aliceArrows):
            if soFarSum > maxScore[0]:
                soFar[0] += numArrows
                maxScore[0] = soFarSum
                bobArrows[:] = soFar[:]  # Update bobArrows with the current soFar
                soFar[0] -= numArrows
            return

        if aliceArrows[index] < numArrows:
            soFar[index] = aliceArrows[index] + 1
            self.helper(numArrows - soFar[index], aliceArrows, bobArrows, index + 1, maxScore, soFarSum + index, soFar)
            soFar[index] = 0
        
        self.helper(numArrows, aliceArrows, bobArrows, index + 1, maxScore, soFarSum, soFar)

    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        bobArrows = [0] * 12
        soFar = [0] * 12
        maxScore = [float('-inf')]  # Use a list to mutate its value
        self.helper(numArrows, aliceArrows, bobArrows, 1, maxScore, 0, soFar)
        return bobArrows