Given a binary string s, you can split s into 3 non-empty strings s1, s2, and s3 where s1 + s2 + s3 = s.

Return the number of ways s can be split such that the number of ones is the same in s1, s2, and s3. Since the answer may be too large, return it modulo 109 + 7.

 

Example 1:

Input: s = "10101"
Output: 4
Explanation: There are four ways to split s in 3 parts where each part contain the same number of letters '1'.
"1|010|1"
"1|01|01"
"10|10|1"
"10|1|01"
Example 2:

Input: s = "1001"
Output: 0
Example 3:

Input: s = "0000"
Output: 3
Explanation: There are three ways to split s in 3 parts.
"0|0|00"
"0|00|0"
"00|0|0"
 

Constraints:

3 <= s.length <= 105
s[i] is either '0' or '1'.





class Solution:
    def numWays(self, s: str) -> int:
        MOD = 10**9 + 7
        ones = s.count('1')
        n = len(s)
        if ones % 3 != 0:
            return 0
        if ones == 0:
            return ((n - 1) * (n - 2) // 2) % MOD
        ones //= 3
        count = ones1 = ones2 = 0
        for c in s:
            if c == '1':
                count += 1
            if count == ones:
                ones1 += 1
            if count == 2 * ones:
                ones2 += 1
        return (ones1 * ones2) % MOD
