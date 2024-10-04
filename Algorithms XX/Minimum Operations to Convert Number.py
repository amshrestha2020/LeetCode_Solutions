You are given a 0-indexed integer array nums containing distinct numbers, an integer start, and an integer goal. There is an integer x that is initially set to start, and you want to perform operations on x such that it is converted to goal. You can perform the following operation repeatedly on the number x:

If 0 <= x <= 1000, then for any index i in the array (0 <= i < nums.length), you can set x to any of the following:

x + nums[i]
x - nums[i]
x ^ nums[i] (bitwise-XOR)
Note that you can use each nums[i] any number of times in any order. Operations that set x to be out of the range 0 <= x <= 1000 are valid, but no more operations can be done afterward.

Return the minimum number of operations needed to convert x = start into goal, and -1 if it is not possible.

 

Example 1:

Input: nums = [2,4,12], start = 2, goal = 12
Output: 2
Explanation: We can go from 2 → 14 → 12 with the following 2 operations.
- 2 + 12 = 14
- 14 - 2 = 12
Example 2:

Input: nums = [3,5,7], start = 0, goal = -4
Output: 2
Explanation: We can go from 0 → 3 → -4 with the following 2 operations. 
- 0 + 3 = 3
- 3 - 7 = -4
Note that the last operation sets x out of the range 0 <= x <= 1000, which is valid.
Example 3:

Input: nums = [2,8,16], start = 0, goal = 1
Output: -1
Explanation: There is no way to convert 0 into 1.
 

Constraints:

1 <= nums.length <= 1000
-109 <= nums[i], goal <= 109
0 <= start <= 1000
start != goal
All the integers in nums are distinct.





class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        from collections import deque
        from typing import List


        n = len(nums)  # Get the size of the nums list
        q = deque([start])  # Initialize the queue with the starting value
        ops = 0  # Initialize the operation count
        vis = [0] * 1001  # Initialize a visited list to keep track of visited states
        vis[start] = 1  # Mark the start as visited
        
        while q:
            sz = len(q)  # Get the current size of the queue
            for _ in range(sz):
                x = q.popleft()  # Pop the front element from the queue
                if x == goal:  # Check if we reached the goal
                    return ops
                
                # Iterate through the nums list to perform operations
                for j in range(n):
                    a = x + nums[j]
                    b = x - nums[j]
                    c = x ^ nums[j]
                    
                    # Check if any operation results in the goal
                    if a == goal or b == goal or c == goal:
                        return ops + 1
                    
                    # Push valid states into the queue and mark them as visited
                    if 0 <= a <= 1000 and vis[a] == 0:
                        q.append(a)
                        vis[a] = 1
                    if 0 <= b <= 1000 and vis[b] == 0:
                        q.append(b)
                        vis[b] = 1
                    if 0 <= c <= 1000 and vis[c] == 0:
                        q.append(c)
                        vis[c] = 1
            
            ops += 1  # Increment the operation count
        
        return -1