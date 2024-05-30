You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

Return true if you can make this square and false otherwise.

 

Example 1:


Input: matchsticks = [1,1,2,2,2]
Output: true
Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
Example 2:

Input: matchsticks = [3,3,3,3,4]
Output: false
Explanation: You cannot find a way to form a square with all the matchsticks.
 

Constraints:

1 <= matchsticks.length <= 15
1 <= matchsticks[i] <= 108







class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if not matchsticks:
            return False

        total_length = sum(matchsticks)
        if total_length % 4 != 0:
            return False

        matchsticks.sort(reverse=True)
        target_length = total_length // 4
        sides = [0] * 4

        def dfs(index):
            if index == len(matchsticks):
                return sides[0] == sides[1] == sides[2] == target_length
            for i in range(4):
                if sides[i] + matchsticks[index] > target_length:
                    continue
                sides[i] += matchsticks[index]
                if dfs(index + 1):
                    return True
                sides[i] -= matchsticks[index]
            return False

        return dfs(0)
