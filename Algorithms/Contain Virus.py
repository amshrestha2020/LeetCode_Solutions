A virus is spreading rapidly, and your task is to quarantine the infected area by installing walls.

The world is modeled as an m x n binary grid isInfected, where isInfected[i][j] == 0 represents uninfected cells, and isInfected[i][j] == 1 represents cells contaminated with the virus. A wall (and only one wall) can be installed between any two 4-directionally adjacent cells, on the shared boundary.

Every night, the virus spreads to all neighboring cells in all four directions unless blocked by a wall. Resources are limited. Each day, you can install walls around only one region (i.e., the affected area (continuous block of infected cells) that threatens the most uninfected cells the following night). There will never be a tie.

Return the number of walls used to quarantine all the infected regions. If the world will become fully infected, return the number of walls used.

 

Example 1:


Input: isInfected = [[0,1,0,0,0,0,0,1],[0,1,0,0,0,0,0,1],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0]]
Output: 10
Explanation: There are 2 contaminated regions.
On the first day, add 5 walls to quarantine the viral region on the left. The board after the virus spreads is:

On the second day, add 5 walls to quarantine the viral region on the right. The virus is fully contained.

Example 2:


Input: isInfected = [[1,1,1],[1,0,1],[1,1,1]]
Output: 4
Explanation: Even though there is only one cell saved, there are 4 walls built.
Notice that walls are only built on the shared boundary of two different cells.
Example 3:

Input: isInfected = [[1,1,1,0,0,0,0,0,0],[1,0,1,0,1,1,1,1,1],[1,1,1,0,0,0,0,0,0]]
Output: 13
Explanation: The region on the left only builds two new walls.
 

Constraints:

m == isInfected.length
n == isInfected[i].length
1 <= m, n <= 50
isInfected[i][j] is either 0 or 1.
There is always a contiguous viral region throughout the described process that will infect strictly more uncontaminated squares in the next round.




class Solution:
    def containVirus(self, isInfected):
        step = len(isInfected[0]) + 1
        mk = 0
        mp = [1000] * (step * (len(isInfected) + 2))
        zp = [None] * 2652
        zc = [0] * 2652

        def dfs(p):
            mp[p] = 2
            res = 0
            for nb in [p-step, p-1, p+1, p+step]:
                v = mp[nb]
                if v == mk or v > 1:
                    continue
                if v <= 0:
                    mp[nb] = mk
                    res += 1
                else:
                    res += dfs(nb)
            return res

        def dfs2(p):
            mp[p] = 1000
            res = 0
            for nb in [p-step, p-1, p+1, p+step]:
                v = mp[nb]
                if v == 2:
                    res += dfs2(nb)
                elif v <= 0:
                    res += 1
                    mp[nb] = 0
            return res

        def dfs3(p):
            mp[p] = 1
            for nb in [p-step, p-1, p+1, p+step]:
                v = mp[nb]
                if v == 2:
                    dfs3(nb)
                elif v <= 0:
                    mp[nb] = 1

        p = step
        for r in isInfected:
            for x in r:
                mp[p] = x
                p += 1
            mp[p] = 1000
            p += 1
        mp[p:p+step] = [1000] * step

        lo = step
        hi = lo + step * len(isInfected)
        res = 0
        while True:
            nb = 0
            for p in range(lo, hi):
                if mp[p] == 1:
                    zp[nb] = p
                    mk -= 1
                    zc[nb] = dfs(p)
                    nb += 1
            if nb == 0:
                break

            best = 0
            for i in range(1, nb):
                if zc[i] > zc[best]:
                    best = i
            if zc[best] == 0:
                break
            res += dfs2(zp[best])

            for p in range(lo, hi):
                if mp[p] == 2:
                    dfs3(p)

        return res


