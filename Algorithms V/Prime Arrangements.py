Return the number of permutations of 1 to n so that prime numbers are at prime indices (1-indexed.)

(Recall that an integer is prime if and only if it is greater than 1, and cannot be written as a product of two positive integers both smaller than it.)

Since the answer may be large, return the answer modulo 10^9 + 7.

 

Example 1:

Input: n = 5
Output: 12
Explanation: For example [1,2,5,4,3] is a valid permutation, but [5,2,3,4,1] is not because the prime number 5 is at index 1.
Example 2:

Input: n = 100
Output: 682289015
 

Constraints:

1 <= n <= 100





class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        def primeCount(n):
            sieve = [1] * (n + 1)
            sieve[0] = sieve[1] = 0
            for i in range(2, int(n**0.5) + 1):
                if sieve[i]:
                    for j in range(i*i, n + 1, i):
                        sieve[j] = 0
            return sum(sieve)

        def factorial(n, mod):
            fact = [1] * (n + 1)
            for i in range(1, n + 1):
                fact[i] = fact[i - 1] * i % mod
            return fact

        mod = 10**9 + 7
        primes = primeCount(n)
        fact = factorial(n, mod)
        return fact[primes] * fact[n - primes] % mod
