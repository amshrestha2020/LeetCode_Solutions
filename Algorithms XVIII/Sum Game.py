Alice and Bob take turns playing a game, with Alice starting first.

You are given a string num of even length consisting of digits and '?' characters. On each turn, a player will do the following if there is still at least one '?' in num:

Choose an index i where num[i] == '?'.
Replace num[i] with any digit between '0' and '9'.
The game ends when there are no more '?' characters in num.

For Bob to win, the sum of the digits in the first half of num must be equal to the sum of the digits in the second half. For Alice to win, the sums must not be equal.

For example, if the game ended with num = "243801", then Bob wins because 2+4+3 = 8+0+1. If the game ended with num = "243803", then Alice wins because 2+4+3 != 8+0+3.
Assuming Alice and Bob play optimally, return true if Alice will win and false if Bob will win.

 

Example 1:

Input: num = "5023"
Output: false
Explanation: There are no moves to be made.
The sum of the first half is equal to the sum of the second half: 5 + 0 = 2 + 3.
Example 2:

Input: num = "25??"
Output: true
Explanation: Alice can replace one of the '?'s with '9' and it will be impossible for Bob to make the sums equal.
Example 3:

Input: num = "?3295???"
Output: false
Explanation: It can be proven that Bob will always win. One possible outcome is:
- Alice replaces the first '?' with '9'. num = "93295???".
- Bob replaces one of the '?' in the right half with '9'. num = "932959??".
- Alice replaces one of the '?' in the right half with '2'. num = "9329592?".
- Bob replaces the last '?' in the right half with '7'. num = "93295927".
Bob wins because 9 + 3 + 2 + 9 = 5 + 9 + 2 + 7.
 

Constraints:

2 <= num.length <= 105
num.length is even.
num consists of only digits and '?'.




class Solution:
    def sumGame(self, num: str) -> bool:
        N = len(num)
        
        l_digit_sum = 0
        l_q_count = 0
        r_digit_sum = 0
        r_q_count = 0
        
        for i in range(N):
            if num[i].isdigit():
                if i < N // 2:
                    l_digit_sum += int(num[i])
                else:
                    r_digit_sum += int(num[i])
            else:
                if i < N // 2:
                    l_q_count += 1
                else:
                    r_q_count += 1
        
        # Case 0: Only digits (without '?')
        if (l_q_count + r_q_count) == 0:
            return l_digit_sum != r_digit_sum
        
        # Case 1: Odd number of '?'
        if (l_q_count + r_q_count) % 2 == 1:
            return True
        
        # Case 2: Even number of '?'
        min_q_count = min(l_q_count, r_q_count)
        l_q_count -= min_q_count
        r_q_count -= min_q_count
        
        return l_digit_sum + 9 * l_q_count // 2 != r_digit_sum + 9 * r_q_count // 2        