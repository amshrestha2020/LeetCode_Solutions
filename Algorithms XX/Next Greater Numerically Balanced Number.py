An integer x is numerically balanced if for every digit d in the number x, there are exactly d occurrences of that digit in x.

Given an integer n, return the smallest numerically balanced number strictly greater than n.

 

Example 1:

Input: n = 1
Output: 22
Explanation: 
22 is numerically balanced since:
- The digit 2 occurs 2 times. 
It is also the smallest numerically balanced number strictly greater than 1.
Example 2:

Input: n = 1000
Output: 1333
Explanation: 
1333 is numerically balanced since:
- The digit 1 occurs 1 time.
- The digit 3 occurs 3 times. 
It is also the smallest numerically balanced number strictly greater than 1000.
Note that 1022 cannot be the answer because 0 appeared more than 0 times.
Example 3:

Input: n = 3000
Output: 3133
Explanation: 
3133 is numerically balanced since:
- The digit 1 occurs 1 time.
- The digit 3 occurs 3 times.
It is also the smallest numerically balanced number strictly greater than 3000.
 

Constraints:

0 <= n <= 106



class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        from itertools import permutations

        base = [1, 22, 122, 333, 1333, 4444, 14444, 22333, 55555, 122333, 155555, 224444, 666666]
        res = 1224444  # Default result
        s = str(n)     # Convert n to string for comparison

        for nn in base:
            ss = str(nn)  # Convert the base number to string
            
            if len(ss) < len(s):
                continue  # Skip if ss has fewer digits than s
            
            if len(ss) > len(s):
                res = min(res, nn)  # Update result if ss has more digits than s
            else:
                # Generate all unique permutations of ss
                for perm in set(permutations(ss)):
                    perm_number = int(''.join(perm))
                    if perm_number > n:
                        res = min(res, perm_number)

        return res