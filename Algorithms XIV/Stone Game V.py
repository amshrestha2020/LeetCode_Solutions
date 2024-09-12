There are several stones arranged in a row, and each stone has an associated value which is an integer given in the array stoneValue.

In each round of the game, Alice divides the row into two non-empty rows (i.e. left row and right row), then Bob calculates the value of each row which is the sum of the values of all the stones in this row. Bob throws away the row which has the maximum value, and Alice's score increases by the value of the remaining row. If the value of the two rows are equal, Bob lets Alice decide which row will be thrown away. The next round starts with the remaining row.

The game ends when there is only one stone remaining. Alice's is initially zero.

Return the maximum score that Alice can obtain.

 

Example 1:

Input: stoneValue = [6,2,3,4,5,5]
Output: 18
Explanation: In the first round, Alice divides the row to [6,2,3], [4,5,5]. The left row has the value 11 and the right row has value 14. Bob throws away the right row and Alice's score is now 11.
In the second round Alice divides the row to [6], [2,3]. This time Bob throws away the left row and Alice's score becomes 16 (11 + 5).
The last round Alice has only one choice to divide the row which is [2], [3]. Bob throws away the right row and Alice's score is now 18 (16 + 2). The game ends because only one stone is remaining in the row.
Example 2:

Input: stoneValue = [7,7,7,7,7,7,7]
Output: 28
Example 3:

Input: stoneValue = [4]
Output: 0
 

Constraints:

1 <= stoneValue.length <= 500
1 <= stoneValue[i] <= 106





class Solution:
    def findSum(self, stoneValue):
        return sum(stoneValue)  # returns the sum of the stoneValue Array.

    def findMin(self, stoneValue, start, end, preSum, sum, dp):
        if start == end:  # returns 0 whenever the length of the array equals 1.
            return 0

        if dp[start][end] != -1:  # returns the stored value of the sub problem when the specific values of start and end already solved before.
            return dp[start][end]

        ans = float('-inf')  # Initializing the required maximum score of alice with the minimum possible integer.

        for i in range(start, end):  # Iterating a for loop from the starting index to the ending index to check with all the possible partitions.
            preSum = preSum + stoneValue[i]  # Increment the preSum with value of stoneValue at current index where we are going to make partition.

            if preSum < sum - preSum:
                ans = max(ans, preSum + self.findMin(stoneValue, start, i, 0, preSum, dp))
                # if the preSum(the sum of the array from start index to current index) is less than the remaining part of the array,
                # Then Bob throws away the right array i.e the array with the largest sum,
                # Alice score is increased by preSum(sum of the left array) and parameters of the left array are sent to the recursion.
            elif preSum > sum - preSum:
                ans = max(ans, sum - preSum + self.findMin(stoneValue, i + 1, end, 0, sum - preSum, dp))
                # if the preSum(the sum of the array from start index to current index) is more than the remaining part of the array,
                # Then Bob throws away the left array i.e the array with the largest sum,
                # Alice score is increased by sum-preSum(sum of the right array) and parameters of the right array are sent to the recursion.
            else:
                ans = max(ans, max(preSum + self.findMin(stoneValue, start, i, 0, preSum, dp),
                                   sum - preSum + self.findMin(stoneValue, i + 1, end, 0, sum - preSum, dp)))
                # if the preSum(the sum of left array) and sum-preSum(the sum of the right array) are equal,
                # Then, Bob gives Alice a chance to remove either the left array or the right array,
                # So alice has a chance to get maximum score from either of the arrays,
                # So Alice take the the Max value from both the recursions(recursion calls of both left array and right array).

        dp[start][end] = ans  # store the value of the partition for specific start and end values in the dp array.
        return dp[start][end]

    def stoneGameV(self, stoneValue):
        sum = self.findSum(stoneValue)  # To find Sum of the stoneValue array.

        dp = [[-1 for _ in range(len(stoneValue))] for _ in range(len(stoneValue))]  # A 2D array for memorization.

        return self.findMin(stoneValue, 0, len(stoneValue) - 1, 0, sum, dp)  # function to find Maximum score of alice.
