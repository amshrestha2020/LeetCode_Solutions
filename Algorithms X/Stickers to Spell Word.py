We are given n different types of stickers. Each sticker has a lowercase English word on it.

You would like to spell out the given string target by cutting individual letters from your collection of stickers and rearranging them. You can use each sticker more than once if you want, and you have infinite quantities of each sticker.

Return the minimum number of stickers that you need to spell out target. If the task is impossible, return -1.

Note: In all test cases, all words were chosen randomly from the 1000 most common US English words, and target was chosen as a concatenation of two random words.

 

Example 1:

Input: stickers = ["with","example","science"], target = "thehat"
Output: 3
Explanation:
We can use 2 "with" stickers, and 1 "example" sticker.
After cutting and rearrange the letters of those stickers, we can form the target "thehat".
Also, this is the minimum number of stickers necessary to form the target string.
Example 2:

Input: stickers = ["notice","possible"], target = "basicbasic"
Output: -1
Explanation:
We cannot form the target "basicbasic" from cutting letters from the given stickers.
 

Constraints:

n == stickers.length
1 <= n <= 50
1 <= stickers[i].length <= 10
1 <= target.length <= 15
stickers[i] and target consist of lowercase English letters.



from collections import deque

class Solution:
    def minStickers(self, stickers, target):
        def empty(freq):
            return all(f == 0 for f in freq)
        
        def to_string(freq):
            return ''.join(chr(i + ord('a')) * freq[i] for i in range(len(freq)))
        
        target_naive_count = [0] * 26
        for c in target:
            target_naive_count[ord(c) - ord('a')] += 1
        
        index = [-1] * 26
        N = 0
        for i in range(26):
            if target_naive_count[i] > 0:
                index[i] = N
                N += 1
        
        target_count = [0] * N
        t = 0
        for c in target_naive_count:
            if c > 0:
                target_count[t] = c
                t += 1
        
        stickers_count = [[0] * N for _ in range(len(stickers))]
        for i in range(len(stickers)):
            for c in stickers[i]:
                j = index[ord(c) - ord('a')]
                if j >= 0:
                    stickers_count[i][j] += 1
        
        start = 0
        for i in range(len(stickers)):
            for j in range(start, len(stickers)):
                if j != i:
                    k = 0
                    while k < N and stickers_count[i][k] <= stickers_count[j][k]:
                        k += 1
                    if k == N:
                        stickers_count[i], stickers_count[start] = stickers_count[start], stickers_count[i]
                        start += 1
                        break
        
        Q = deque([tuple(target_count)])
        visited = set()
        steps = 0
        
        while Q:
            steps += 1
            for _ in range(len(Q)):
                freq = list(Q.popleft())
                cur = to_string(freq)
                if cur in visited:
                    continue
                visited.add(cur)
                
                first = ord(cur[0]) - ord('a')
                for i in range(start, len(stickers)):
                    if stickers_count[i][first] > 0:
                        next_freq = freq[:]
                        for j in range(N):
                            next_freq[j] = max(next_freq[j] - stickers_count[i][j], 0)
                        if empty(next_freq):
                            return steps
                        Q.append(tuple(next_freq))
        
        return -1

# Test cases
solution = Solution()
print(solution.minStickers(["with", "example", "science"], "thehat"))  # Output: 3
print(solution.minStickers(["notice", "possible"], "basicbasic"))     # Output: -1
