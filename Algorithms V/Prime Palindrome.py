Given an integer n, return the smallest prime palindrome greater than or equal to n.

An integer is prime if it has exactly two divisors: 1 and itself. Note that 1 is not a prime number.

For example, 2, 3, 5, 7, 11, and 13 are all primes.
An integer is a palindrome if it reads the same from left to right as it does from right to left.

For example, 101 and 12321 are palindromes.
The test cases are generated so that the answer always exists and is in the range [2, 2 * 108].

 

Example 1:

Input: n = 6
Output: 7
Example 2:

Input: n = 8
Output: 11
Example 3:

Input: n = 13
Output: 101
 

Constraints:

1 <= n <= 108




class Solution:
    def primePalindrome(self, n: int) -> int:
        def is_prime(x):
            if x < 2:
                return False
            if x in (2, 3):
                return True
            if x % 2 == 0 or x % 3 == 0:
                return False
            i = 5
            while i * i <= x:
                if x % i == 0 or x % (i + 2) == 0:
                    return False
                i += 6
            return True

        def generate_palindromes(length):
            if length == 1:
                for i in range(10):
                    yield i
            elif length % 2 == 0:
                half_len = length // 2
                start = 10 ** (half_len - 1)
                end = 10 ** half_len
                for i in range(start, end):
                    s = str(i)
                    yield int(s + s[::-1])
            else:
                half_len = length // 2
                start = 10 ** (half_len)
                end = 10 ** (half_len + 1)
                for i in range(start, end):
                    s = str(i)
                    yield int(s + s[-2::-1])

        if 8 <= n <= 11:
            return 11

        length = len(str(n))
        while True:
            for pal in generate_palindromes(length):
                if pal >= n and is_prime(pal):
                    return pal
            length += 1

# Example usage:
solution = Solution()
print(solution.primePalindrome(6))     # Output: 7
print(solution.primePalindrome(8))     # Output: 11
print(solution.primePalindrome(13))    # Output: 101
print(solution.primePalindrome(9989900))  # Output: 100030001
