Given the strings s1 and s2 of size n and the string evil, return the number of good strings.

A good string has size n, it is alphabetically greater than or equal to s1, it is alphabetically smaller than or equal to s2, and it does not contain the string evil as a substring. Since the answer can be a huge number, return this modulo 109 + 7.

 

Example 1:

Input: n = 2, s1 = "aa", s2 = "da", evil = "b"
Output: 51 
Explanation: There are 25 good strings starting with 'a': "aa","ac","ad",...,"az". Then there are 25 good strings starting with 'c': "ca","cc","cd",...,"cz" and finally there is one good string starting with 'd': "da". 
Example 2:

Input: n = 8, s1 = "leetcode", s2 = "leetgoes", evil = "leet"
Output: 0 
Explanation: All strings greater than or equal to s1 and smaller than or equal to s2 start with the prefix "leet", therefore, there is not any good string.
Example 3:

Input: n = 2, s1 = "gx", s2 = "gz", evil = "x"
Output: 2
 

Constraints:

s1.length == n
s2.length == n
s1 <= s2
1 <= n <= 500
1 <= evil.length <= 50
All strings consist of lowercase English letters.





class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        MOD = 10**9 + 7
        m = len(evil)
        dp = [[[[-1]*m for _ in range(2)] for _ in range(2)] for _ in range(n+1)]
        prefix = [0]*m
        j = 0
        for i in range(1, m):
            while j > 0 and evil[i] != evil[j]:
                j = prefix[j-1]
            if evil[i] == evil[j]:
                j += 1
            prefix[i] = j

        def solve(idx, f1, f2, evilMatched):
            if evilMatched == m:
                return 0
            if idx == n:
                return 1
            if dp[idx][f1][f2][evilMatched] != -1:
                return dp[idx][f1][f2][evilMatched]
            res = 0
            for c in range(ord('a'), ord('z')+1):
                if f1 and c < ord(s1[idx]):
                    continue
                if f2 and c > ord(s2[idx]):
                    continue
                j = evilMatched
                while j > 0 and chr(c) != evil[j]:
                    j = prefix[j-1]
                if chr(c) == evil[j]:
                    j += 1
                res += solve(idx+1, f1 and c == ord(s1[idx]), f2 and c == ord(s2[idx]), j)
                res %= MOD
            dp[idx][f1][f2][evilMatched] = res
            return res

        return solve(0, 1, 1, 0)
