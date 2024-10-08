You are given a string num consisting of digits only.

Return the largest palindromic integer (in the form of a string) that can be formed using digits taken from num. It should not contain leading zeroes.

Notes:

You do not need to use all the digits of num, but you must use at least one digit.
The digits can be reordered.
 

Example 1:

Input: num = "444947137"
Output: "7449447"
Explanation: 
Use the digits "4449477" from "444947137" to form the palindromic integer "7449447".
It can be shown that "7449447" is the largest palindromic integer that can be formed.
Example 2:

Input: num = "00009"
Output: "9"
Explanation: 
It can be shown that "9" is the largest palindromic integer that can be formed.
Note that the integer returned should not contain leading zeroes.
 

Constraints:

1 <= num.length <= 105
num consists of digits.





class Solution:
    def largestPalindromic(self, num: str) -> str:
        freq = {}
        for char in num:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

        # Convert the frequency dictionary into a sorted list of digit-count pairs
        pairs = sorted([(int(k), v) for k, v in freq.items()], reverse=True)

        ans = []
        middle = ""

        # Add the first half of the palindrome by adding pairs of digits
        for k, v in pairs:
            if k > 0 and v > 1:
                ans.append(str(k) * (v // 2))

        # Handle the case of zeros, if they are available and can be paired
        if ans and '0' in freq and freq['0'] > 1:
            ans.append('0' * (freq['0'] // 2))

        # Find the middle character (the largest one that appears an odd number of times)
        for k, v in pairs:
            if v % 2 != 0:
                middle = str(k)
                break

        # If no middle is found and ans is empty, middle should be zero
        if not middle and not ans:
            middle = '0'

        # Join the first half, middle, and reversed first half to form the largest palindrome
        return ''.join(ans) + middle + ''.join(ans[::-1])        