Suppose you have n integers labeled 1 through n. A permutation of those n integers perm (1-indexed) is considered a beautiful arrangement if for every i (1 <= i <= n), either of the following is true:

perm[i] is divisible by i.
i is divisible by perm[i].
Given an integer n, return the number of the beautiful arrangements that you can construct.

 

Example 1:

Input: n = 2
Output: 2
Explanation: 
The first beautiful arrangement is [1,2]:
    - perm[1] = 1 is divisible by i = 1
    - perm[2] = 2 is divisible by i = 2
The second beautiful arrangement is [2,1]:
    - perm[1] = 2 is divisible by i = 1
    - i = 2 is divisible by perm[2] = 1
Example 2:

Input: n = 1
Output: 1
 

Constraints:

1 <= n <= 15



class Solution:
    def countArrangement(self, n: int) -> int:
        self.count = 0
        self.visited = [False] * (n + 1)
        self.calculate(n, 1)
        return self.count

    def calculate(self, N, pos):
        if pos > N:
            self.count += 1
        for i in range(1, N + 1):
            if not self.visited[i] and (pos % i == 0 or i % pos == 0):
                self.visited[i] = True
                self.calculate(N, pos + 1)
                self.visited[i] = False


