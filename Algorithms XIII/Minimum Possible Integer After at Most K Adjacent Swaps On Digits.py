You are given a string num representing the digits of a very large integer and an integer k. You are allowed to swap any two adjacent digits of the integer at most k times.

Return the minimum integer you can obtain also as a string.

 

Example 1:


Input: num = "4321", k = 4
Output: "1342"
Explanation: The steps to obtain the minimum integer from 4321 with 4 adjacent swaps are shown.
Example 2:

Input: num = "100", k = 1
Output: "010"
Explanation: It's ok for the output to have leading zeros, but the input is guaranteed not to have any leading zeros.
Example 3:

Input: num = "36789", k = 1000
Output: "36789"
Explanation: We can keep the number without any swaps.
 

Constraints:

1 <= num.length <= 3 * 104
num consists of only digits and does not contain leading zeros.
1 <= k <= 109




from collections import deque

class Solution:
    def minInteger(self, num: str, k: int) -> str:
        # pqs stores the location of each digit.
        pqs = [deque() for _ in range(10)]

        for i in range(len(num)):
            pqs[int(num[i])].append(i)

        ans = ""
        seg = SegmentTree(len(num))

        for i in range(len(num)):
            # At each location, try to place 0....9
            for digit in range(10):
                # is there any occurrence of digit left?
                if pqs[digit]:
                    # yes, there is a occurrence of digit at pos
                    pos = pqs[digit][0]
                    # Since few numbers already shifted to left, this `pos` might be outdated.
                    # we try to find how many number already got shifted that were to the left of pos.
                    shift = seg.getCountLessThan(pos)
                    # (pos - shift) is number of steps to make digit move from pos to i.
                    if pos - shift <= k:
                        k -= pos - shift
                        seg.add(pos)  # Add pos to our segment tree.
                        pqs[digit].popleft()
                        ans += str(digit)
                        break

        return ans


class SegmentTree:
    def __init__(self, max_val):
        self.nodes = [0] * (4 * max_val)
        self.n = max_val

    def add(self, num):
        self._addUtil(num, 0, self.n, 0)

    def _addUtil(self, num, l, r, node):
        if num < l or num > r:
            return
        if l == r:
            self.nodes[node] += 1
            return
        mid = (l + r) // 2
        self._addUtil(num, l, mid, 2 * node + 1)
        self._addUtil(num, mid + 1, r, 2 * node + 2)
        self.nodes[node] = self.nodes[2 * node + 1] + self.nodes[2 * node + 2]

    # Essentially it tells count of numbers < num.
    def getCountLessThan(self, num):
        return self._getUtil(0, num, 0, self.n, 0)

    def _getUtil(self, ql, qr, l, r, node):
        if qr < l or ql > r:
            return 0
        if ql <= l and qr >= r:
            return self.nodes[node]

        mid = (l + r) // 2
        return self._getUtil(ql, qr, l, mid, 2 * node + 1) + self._getUtil(ql, qr, mid + 1, r, 2 * node + 2)
