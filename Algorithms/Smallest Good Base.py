Given an integer n represented as a string, return the smallest good base of n.

We call k >= 2 a good base of n, if all digits of n base k are 1's.

 

Example 1:

Input: n = "13"
Output: "3"
Explanation: 13 base 3 is 111.
Example 2:

Input: n = "4681"
Output: "8"
Explanation: 4681 base 8 is 11111.
Example 3:

Input: n = "1000000000000000000"
Output: "999999999999999999"
Explanation: 1000000000000000000 base 999999999999999999 is 11.
 

Constraints:

n is an integer in the range [3, 1018].
n does not contain any leading zeros.



class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n = int(n)
        max_m = int(math.log(n, 2))  # Maximum number of 1's in the base-k representation
        for m in range(max_m, 1, -1):
            k = int(n ** m ** -1)  # Calculate the base k
            if (k**(m+1) - 1) // (k - 1) == n:  # Check if n can be represented with all 1's in base k
                return str(k)
        return str(n - 1)  # If no good base is found, return n-1

# Example usage:
# sol = Solution()
# print(sol.smallestGoodBase("13"))  # Output: "3"
# print(sol.smallestGoodBase("4681"))  # Output: "8"
# print(sol.smallestGoodBase("1000000000000000000"))  # Output: "999999999999999999"

