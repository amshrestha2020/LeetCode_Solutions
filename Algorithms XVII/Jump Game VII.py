You are given a 0-indexed binary string s and two integers minJump and maxJump. In the beginning, you are standing at index 0, which is equal to '0'. You can move from index i to index j if the following conditions are fulfilled:

i + minJump <= j <= min(i + maxJump, s.length - 1), and
s[j] == '0'.
Return true if you can reach index s.length - 1 in s, or false otherwise.

 

Example 1:

Input: s = "011010", minJump = 2, maxJump = 3
Output: true
Explanation:
In the first step, move from index 0 to index 3. 
In the second step, move from index 3 to index 5.
Example 2:

Input: s = "01101110", minJump = 2, maxJump = 3
Output: false
 

Constraints:

2 <= s.length <= 105
s[i] is either '0' or '1'.
s[0] == '0'
1 <= minJump <= maxJump < s.length



class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[n - 1] == '1':
            return False  # Cannot end at '1'

        # DP array to keep track of reachable positions
        dp = [False] * n
        dp[0] = True
        
        # This variable will keep track of the number of reachable positions within the window
        window_sum = 0
        
        for i in range(1, n):
            # Maintain the window sum of reachable positions in the range [i - maxJump, i - minJump]
            if i - minJump >= 0 and dp[i - minJump]:
                window_sum += 1
            if i - maxJump - 1 >= 0 and dp[i - maxJump - 1]:
                window_sum -= 1
            
            # If there's any reachable index in the range, mark current index as reachable
            if window_sum > 0 and s[i] == '0':
                dp[i] = True
        
        return dp[n - 1]        