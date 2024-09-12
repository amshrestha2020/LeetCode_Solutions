A game on an undirected graph is played by two players, Mouse and Cat, who alternate turns.

The graph is given as follows: graph[a] is a list of all nodes b such that ab is an edge of the graph.

The mouse starts at node 1 and goes first, the cat starts at node 2 and goes second, and there is a hole at node 0.

During each player's turn, they must travel along one edge of the graph that meets where they are.  For example, if the Mouse is at node 1, it must travel to any node in graph[1].

Additionally, it is not allowed for the Cat to travel to the Hole (node 0).

Then, the game can end in three ways:

If ever the Cat occupies the same node as the Mouse, the Cat wins.
If ever the Mouse reaches the Hole, the Mouse wins.
If ever a position is repeated (i.e., the players are in the same position as a previous turn, and it is the same player's turn to move), the game is a draw.
Given a graph, and assuming both players play optimally, return

1 if the mouse wins the game,
2 if the cat wins the game, or
0 if the game is a draw.
 

Example 1:


Input: graph = [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]
Output: 0
Example 2:


Input: graph = [[1,3],[0],[3],[0,2]]
Output: 1
 

Constraints:

3 <= graph.length <= 50
1 <= graph[i].length < graph.length
0 <= graph[i][j] < graph.length
graph[i][j] != i
graph[i] is unique.
The mouse and the cat can always move. 






from collections import deque

class Solution:
    def catMouseGame(self, graph):
        n = len(graph)
        DRAW = 0
        MOUSE_WIN = 1
        CAT_WIN = 2
        
        # dp[mouse][cat][turn]: the outcome of the state
        dp = [[[DRAW] * 2 for _ in range(n)] for _ in range(n)]
        
        # Base cases:
        for i in range(n):
            for turn in range(2):
                dp[0][i][turn] = MOUSE_WIN  # Mouse wins by reaching the hole
                dp[i][i][turn] = CAT_WIN    # Cat wins by catching the mouse

        queue = deque()
        
        for i in range(1, n):
            for turn in range(2):
                dp[i][0][turn] = MOUSE_WIN
                queue.append((i, 0, turn, MOUSE_WIN))
                dp[0][i][turn] = MOUSE_WIN
                queue.append((0, i, turn, MOUSE_WIN))
                dp[i][i][turn] = CAT_WIN
                queue.append((i, i, turn, CAT_WIN))
        
        def parents(mouse, cat, turn):
            if turn == 1:
                for m in graph[mouse]:
                    yield (m, cat, 0)
            else:
                for c in graph[cat]:
                    if c != 0:
                        yield (mouse, c, 1)
        
        while queue:
            mouse, cat, turn, result = queue.popleft()
            for m, c, t in parents(mouse, cat, turn):
                if dp[m][c][t] == DRAW:
                    if result == MOUSE_WIN and t == 0:
                        dp[m][c][t] = MOUSE_WIN
                        queue.append((m, c, t, MOUSE_WIN))
                    elif result == CAT_WIN and t == 1:
                        dp[m][c][t] = CAT_WIN
                        queue.append((m, c, t, CAT_WIN))
                    else:
                        draw_condition = all(
                            dp[m2][c][1 - t] == CAT_WIN for m2 in graph[m]
                        ) if t == 0 else all(
                            dp[m][c2][1 - t] == MOUSE_WIN for c2 in graph[c] if c2 != 0
                        )
                        if draw_condition:
                            dp[m][c][t] = result
                            queue.append((m, c, t, result))
        
        return dp[1][2][0]

# Example usage
sol = Solution()
print(sol.catMouseGame([[2, 5], [3], [0, 4, 5], [1, 4, 5], [2, 3], [0, 2, 3]]))  # Output: 0
print(sol.catMouseGame([[1, 3], [0], [3], [0, 2]]))  # Output: 1
