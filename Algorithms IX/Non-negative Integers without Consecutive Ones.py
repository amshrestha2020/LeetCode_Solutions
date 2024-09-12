Given a positive integer n, return the number of the integers in the range [0, n] whose binary representations do not contain consecutive ones.

 

Example 1:

Input: n = 5
Output: 5
Explanation:
Here are the non-negative integers <= 5 with their corresponding binary representations:
0 : 0
1 : 1
2 : 10
3 : 11
4 : 100
5 : 101
Among them, only integer 3 disobeys the rule (two consecutive ones) and the other 5 satisfy the rule. 
Example 2:

Input: n = 1
Output: 2
Example 3:

Input: n = 2
Output: 3
 

Constraints:

1 <= n <= 109




class Solution:
    def findIntegers(self, n: int) -> int:
        x = bin(n)[2:]
        l = len(x)

        # dp[i] stores the count of valid strings of length i.
        # Here dp[i][0] represents the count of valid strings ending with 0,
        # and dp[i][1] represents the count of valid strings ending with 1.
        dp = [[0, 0] for _ in range(l + 1)]
        dp[1][0] = dp[1][1] = 1

        for i in range(2, l + 1):
            # If we put a '0' at the end of all valid strings of length i-1,
            # we get a valid string of length i.
            dp[i][0] = dp[i - 1][0] + dp[i - 1][1]

            # If we put a '1' at the end of all valid strings of length i-1
            # that ends with '0', we get a valid string of length i.
            dp[i][1] = dp[i - 1][0]

        # Count of all valid strings of length l.
        ans = dp[l][0] + dp[l][1]

        # Now we need to handle the case where the input number itself has no consecutive ones.
        for i in range(1, l):
            # If there are consecutive ones in the original number, we don't need to consider the rest.
            if x[i] == '1' and x[i - 1] == '1':
                break

            # If there are consecutive zeros in the original number, we should subtract the count of valid numbers with length i+1.
            if x[i] == '0' and x[i - 1] == '0':
                ans -= dp[l - i][1]

        return ans
