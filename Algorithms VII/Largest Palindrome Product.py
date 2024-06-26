
Topics
Companies
Given an integer n, return the largest palindromic integer that can be represented as the product of two n-digits integers. Since the answer can be very large, return it modulo 1337.

 

Example 1:

Input: n = 2
Output: 987
Explanation: 99 x 91 = 9009, 9009 % 1337 = 987
Example 2:

Input: n = 1
Output: 9
 

Constraints:

1 <= n <= 8




class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9
        upper = 10 ** n - 1
        lower = upper // 10
        for i in range(upper, lower, -1):
            palindrome = int(str(i) + str(i)[::-1])
            j = upper
            while j * j >= palindrome:
                if palindrome % j == 0:
                    return palindrome % 1337
                j -= 1
        return -1
