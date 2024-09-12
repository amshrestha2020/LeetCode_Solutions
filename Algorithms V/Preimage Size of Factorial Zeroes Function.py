Let f(x) be the number of zeroes at the end of x!. Recall that x! = 1 * 2 * 3 * ... * x and by convention, 0! = 1.

For example, f(3) = 0 because 3! = 6 has no zeroes at the end, while f(11) = 2 because 11! = 39916800 has two zeroes at the end.
Given an integer k, return the number of non-negative integers x have the property that f(x) = k.

 

Example 1:

Input: k = 0
Output: 5
Explanation: 0!, 1!, 2!, 3!, and 4! end with k = 0 zeroes.
Example 2:

Input: k = 5
Output: 0
Explanation: There is no x such that x! ends in k = 5 zeroes.
Example 3:

Input: k = 3
Output: 5
 

Constraints:

0 <= k <= 109




class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def f(x):
            return x // 5 + f(x // 5) if x > 0 else 0

        left, right = 0, 10 * k + 1
        while left < right:
            mid = (left + right) // 2
            if f(mid) < k:
                left = mid + 1
            else:
                right = mid

        return 5 if f(left) == k else 0

