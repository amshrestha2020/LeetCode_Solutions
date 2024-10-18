You are given a positive integer n.

Continuously replace n with the sum of its prime factors.

Note that if a prime factor divides n multiple times, it should be included in the sum as many times as it divides n.
Return the smallest value n will take on.

 

Example 1:

Input: n = 15
Output: 5
Explanation: Initially, n = 15.
15 = 3 * 5, so replace n with 3 + 5 = 8.
8 = 2 * 2 * 2, so replace n with 2 + 2 + 2 = 6.
6 = 2 * 3, so replace n with 2 + 3 = 5.
5 is the smallest value n will take on.
Example 2:

Input: n = 3
Output: 3
Explanation: Initially, n = 3.
3 is the smallest value n will take on.
 

Constraints:

2 <= n <= 105




class Solution:
    def smallestValue(self, n: int) -> int:
        def sum_of_prime_factors(n):
            sum_factors = 0
            # Check for number of 2s that divide n
            while n % 2 == 0:
                sum_factors += 2
                n //= 2
            
            # n must be odd at this point, check for odd factors from 3 onward
            for i in range(3, int(n**0.5) + 1, 2):
                while n % i == 0:
                    sum_factors += i
                    n //= i
            
            # If n is a prime number greater than 2
            if n > 2:
                sum_factors += n
            
            return sum_factors
        
        while True:
            new_n = sum_of_prime_factors(n)
            if new_n == n:
                break
            n = new_n
            
        return n        