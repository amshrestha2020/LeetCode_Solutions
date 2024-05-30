Given an integer n, your task is to count how many strings of length n can be formed under the following rules:

Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
Each vowel 'a' may only be followed by an 'e'.
Each vowel 'e' may only be followed by an 'a' or an 'i'.
Each vowel 'i' may not be followed by another 'i'.
Each vowel 'o' may only be followed by an 'i' or a 'u'.
Each vowel 'u' may only be followed by an 'a'.
Since the answer may be too large, return it modulo 10^9 + 7.

 

Example 1:

Input: n = 1
Output: 5
Explanation: All possible strings are: "a", "e", "i" , "o" and "u".
Example 2:

Input: n = 2
Output: 10
Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".
Example 3: 

Input: n = 5
Output: 68
 

Constraints:

1 <= n <= 2 * 10^4



class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10**9 + 7
        # dp[i][j] is the number of strings of length i that ends with the j-th vowel
        dp = [[0]*5 for _ in range(n+1)]
        # Initialization: there is one string of length 1 that ends with each vowel
        for j in range(5):
            dp[1][j] = 1
        # Transition rules
        for i in range(2, n+1):
            dp[i][0] = dp[i-1][1] % MOD  # 'a' can only be followed by 'e'
            dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % MOD  # 'e' can be followed by 'a' or 'i'
            dp[i][2] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][3] + dp[i-1][4]) % MOD  # 'i' can be followed by any vowel except 'i'
            dp[i][3] = (dp[i-1][2] + dp[i-1][4]) % MOD  # 'o' can be followed by 'i' or 'u'
            dp[i][4] = dp[i-1][0] % MOD  # 'u' can only be followed by 'a'
        # The answer is the sum of strings of length n that end with any vowel
        return sum(dp[n]) % MOD
