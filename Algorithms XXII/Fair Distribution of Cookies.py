You are given an integer array cookies, where cookies[i] denotes the number of cookies in the ith bag. You are also given an integer k that denotes the number of children to distribute all the bags of cookies to. All the cookies in the same bag must go to the same child and cannot be split up.

The unfairness of a distribution is defined as the maximum total cookies obtained by a single child in the distribution.

Return the minimum unfairness of all distributions.

 

Example 1:

Input: cookies = [8,15,10,20,8], k = 2
Output: 31
Explanation: One optimal distribution is [8,15,8] and [10,20]
- The 1st child receives [8,15,8] which has a total of 8 + 15 + 8 = 31 cookies.
- The 2nd child receives [10,20] which has a total of 10 + 20 = 30 cookies.
The unfairness of the distribution is max(31,30) = 31.
It can be shown that there is no distribution with an unfairness less than 31.
Example 2:

Input: cookies = [6,1,3,2,2,4,1,2], k = 3
Output: 7
Explanation: One optimal distribution is [6,1], [3,2,2], and [4,1,2]
- The 1st child receives [6,1] which has a total of 6 + 1 = 7 cookies.
- The 2nd child receives [3,2,2] which has a total of 3 + 2 + 2 = 7 cookies.
- The 3rd child receives [4,1,2] which has a total of 4 + 1 + 2 = 7 cookies.
The unfairness of the distribution is max(7,7,7) = 7.
It can be shown that there is no distribution with an unfairness less than 7.
 

Constraints:

2 <= cookies.length <= 8
1 <= cookies[i] <= 105
2 <= k <= cookies.length




class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        distribute = [0] * k  # Initialize the distribution array
        return self.DFS(0, distribute, cookies, k, k)

    def DFS(self, i: int, distribute: List[int], cookies: List[int], k: int, zeroCount: int) -> int:
        # If there are not enough cookies remaining, return infinity as it leads to an invalid distribution.
        if len(cookies) - i < zeroCount:
            return float('inf')

        # If all cookies have been distributed, return the unfairness of this distribution.
        if i == len(cookies):
            unfairness = max(distribute)
            return unfairness
        
        # Try to distribute the i-th cookie to each child and update the answer as the minimum unfairness
        answer = float('inf')
        for j in range(k):
            zeroCount -= 1 if distribute[j] == 0 else 0
            distribute[j] += cookies[i]
            
            # Recursively distribute the next cookie
            answer = min(answer, self.DFS(i + 1, distribute, cookies, k, zeroCount))
            
            # Backtrack
            distribute[j] -= cookies[i]
            zeroCount += 1 if distribute[j] == 0 else 0
        
        return answer    