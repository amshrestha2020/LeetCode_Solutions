You are given three positive integers: n, index, and maxSum. You want to construct an array nums (0-indexed) that satisfies the following conditions:

nums.length == n
nums[i] is a positive integer where 0 <= i < n.
abs(nums[i] - nums[i+1]) <= 1 where 0 <= i < n-1.
The sum of all the elements of nums does not exceed maxSum.
nums[index] is maximized.
Return nums[index] of the constructed array.

Note that abs(x) equals x if x >= 0, and -x otherwise.

 

Example 1:

Input: n = 4, index = 2,  maxSum = 6
Output: 2
Explanation: nums = [1,2,2,1] is one array that satisfies all the conditions.
There are no arrays that satisfy all the conditions and have nums[2] == 3, so 2 is the maximum nums[2].
Example 2:

Input: n = 6, index = 1,  maxSum = 10
Output: 3
 

Constraints:

1 <= n <= maxSum <= 109
0 <= index < n






class Solution:
    def trapezoid(self, n, m=1):
        """Calculate the sum of integers from m to n."""
        return (n - m + 1) * (n + m) // 2

    def area(self, index, x, n):
        """Calculate the total sum of elements if nums[index] = x."""
        total = 0

        # Calculate sum for elements to the left of `index`
        if x > index:
            total += self.trapezoid(x, x - index)
        else:
            total += self.trapezoid(x) + (index - x + 1)

        # Calculate sum for elements to the right of `index`
        if x >= n - index:
            total += self.trapezoid(x - 1, x - n + index + 1)
        else:
            total += self.trapezoid(x - 1) + (n - index - x)

        return total

    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        """Binary search to find the maximum possible value for nums[index]."""
        left, right = 1, maxSum
        result = 1

        while left <= right:
            mid = left + (right - left) // 2
            if self.area(index, mid, n) <= maxSum:
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        return result