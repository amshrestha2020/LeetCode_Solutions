There are n people and 40 types of hats labeled from 1 to 40.

Given a 2D integer array hats, where hats[i] is a list of all hats preferred by the ith person.

Return the number of ways that the n people wear different hats to each other.

Since the answer may be too large, return it modulo 109 + 7.

 

Example 1:

Input: hats = [[3,4],[4,5],[5]]
Output: 1
Explanation: There is only one way to choose hats given the conditions. 
First person choose hat 3, Second person choose hat 4 and last one hat 5.
Example 2:

Input: hats = [[3,5,1],[3,5]]
Output: 4
Explanation: There are 4 ways to choose hats:
(3,5), (5,3), (1,3) and (1,5)
Example 3:

Input: hats = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
Output: 24
Explanation: Each person can choose hats labeled from 1 to 4.
Number of Permutations of (1,2,3,4) = 24.
 

Constraints:

n == hats.length
1 <= n <= 10
1 <= hats[i].length <= 40
1 <= hats[i][j] <= 40
hats[i] contains a list of unique integers.



from typing import List

class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(hats)
        hat_to_people = [[] for _ in range(41)]
        for i in range(n):
            for hat in hats[i]:
                hat_to_people[hat].append(i)
        dp = [0] * (1 << n)
        dp[0] = 1
        for hat in range(1, 41):
            old_dp = dp[:]
            for state in range(1 << n):
                for person in hat_to_people[hat]:
                    if ((state >> person) & 1) == 1:
                        continue
                    new_state = state | (1 << person)
                    dp[new_state] = (dp[new_state] + old_dp[state]) % MOD
        return dp[(1 << n) - 1]
