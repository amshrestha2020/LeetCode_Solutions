Given an array of integers arr, you are initially positioned at the first index of the array.

In one step you can jump from index i to index:

i + 1 where: i + 1 < arr.length.
i - 1 where: i - 1 >= 0.
j where: arr[i] == arr[j] and i != j.
Return the minimum number of steps to reach the last index of the array.

Notice that you can not jump outside of the array at any time.

 

Example 1:

Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
Output: 3
Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is the last index of the array.
Example 2:

Input: arr = [7]
Output: 0
Explanation: Start index is the last index. You do not need to jump.
Example 3:

Input: arr = [7,6,9,6,9,6,9,7]
Output: 1
Explanation: You can jump directly from index 0 to index 7 which is last index of the array.
 

Constraints:

1 <= arr.length <= 5 * 104
-108 <= arr[i] <= 108






from collections import defaultdict, deque

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 0

        graph = defaultdict(list)
        for i, num in enumerate(arr):
            graph[num].append(i)

        queue = deque([0])  # start BFS from index 0
        visited = set()
        steps = 0

        while queue:
            for _ in range(len(queue)):
                idx = queue.popleft()
                if idx == len(arr) - 1:  # reached the last index
                    return steps

                # jump to the next or previous index
                for next_idx in [idx - 1, idx + 1]:
                    if 0 <= next_idx < len(arr) and next_idx not in visited:
                        visited.add(next_idx)
                        queue.append(next_idx)

                # jump to any index with the same value
                while graph[arr[idx]]:
                    same_val_idx = graph[arr[idx]].pop()
                    if same_val_idx != idx and same_val_idx not in visited:
                        visited.add(same_val_idx)
                        queue.append(same_val_idx)

            steps += 1

        return steps
