Alice is texting Bob using her phone. The mapping of digits to letters is shown in the figure below.


In order to add a letter, Alice has to press the key of the corresponding digit i times, where i is the position of the letter in the key.

For example, to add the letter 's', Alice has to press '7' four times. Similarly, to add the letter 'k', Alice has to press '5' twice.
Note that the digits '0' and '1' do not map to any letters, so Alice does not use them.
However, due to an error in transmission, Bob did not receive Alice's text message but received a string of pressed keys instead.

For example, when Alice sent the message "bob", Bob received the string "2266622".
Given a string pressedKeys representing the string received by Bob, return the total number of possible text messages Alice could have sent.

Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: pressedKeys = "22233"
Output: 8
Explanation:
The possible text messages Alice could have sent are:
"aaadd", "abdd", "badd", "cdd", "aaae", "abe", "bae", and "ce".
Since there are 8 possible messages, we return 8.
Example 2:

Input: pressedKeys = "222222222222222222222222222222222222"
Output: 82876089
Explanation:
There are 2082876103 possible text messages Alice could have sent.
Since we need to return the answer modulo 109 + 7, we return 2082876103 % (109 + 7) = 82876089.
 

Constraints:

1 <= pressedKeys.length <= 105
pressedKeys only consists of digits from '2' - '9'.




class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        mod = int(1e9 + 7)  # Define modulo value

        # Function to calculate the number of letters for the given digit
        def cal(c):
            return 4 if c == '7' or c == '9' else 3

        n = len(pressedKeys)  # Length of the input string
        dp = [0] * (n + 1)  # Initialize an array to store counts
        dp[0] = 1  # Base case: Empty string has one possibility
        
        # Loop through each character of the string
        for i in range(n):
            # Loop through possible lengths of substrings
            for j in range(1, cal(pressedKeys[i]) + 1):
                len_substr = i - j + 1  # Calculate length of substring
                if len_substr < 0 or pressedKeys[i] != pressedKeys[len_substr]: 
                    break  # Break if length is invalid or character doesn't match
                dp[i + 1] += dp[i + 1 - j]  # Update count for current position
            
            dp[i + 1] %= mod  # Apply modulo after each iteration
        
        return dp[n]         