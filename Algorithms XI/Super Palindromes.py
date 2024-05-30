Let's say a positive integer is a super-palindrome if it is a palindrome, and it is also the square of a palindrome.

Given two positive integers left and right represented as strings, return the number of super-palindromes integers in the inclusive range [left, right].

 

Example 1:

Input: left = "4", right = "1000"
Output: 4
Explanation: 4, 9, 121, and 484 are superpalindromes.
Note that 676 is not a superpalindrome: 26 * 26 = 676, but 26 is not a palindrome.
Example 2:

Input: left = "1", right = "2"
Output: 1
 

Constraints:

1 <= left.length, right.length <= 18
left and right consist of only digits.
left and right cannot have leading zeros.
left and right represent integers in the range [1, 1018 - 1].
left is less than or equal to right.






class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        L = int(left)
        R = int(right)
        MAGIC = 100000
        ans = 0

        # count odd length
        for x in range(MAGIC):
            s = str(x)
            t = s + s[-2::-1]
            v = int(t)**2
            if v > R: break
            v_str = str(v)
            if v >= L and v_str == v_str[::-1]: ans += 1

        # count even length
        for x in range(MAGIC):
            s = str(x)
            t = s + s[::-1]
            v = int(t)**2
            if v > R: break
            v_str = str(v)
            if v >= L and v_str == v_str[::-1]: ans += 1

        return ans
