There is a special kind of apple tree that grows apples every day for n days. On the ith day, the tree grows apples[i] apples that will rot after days[i] days, that is on day i + days[i] the apples will be rotten and cannot be eaten. On some days, the apple tree does not grow any apples, which are denoted by apples[i] == 0 and days[i] == 0.

You decided to eat at most one apple a day (to keep the doctors away). Note that you can keep eating after the first n days.

Given two integer arrays days and apples of length n, return the maximum number of apples you can eat.

 

Example 1:

Input: apples = [1,2,3,5,2], days = [3,2,1,4,2]
Output: 7
Explanation: You can eat 7 apples:
- On the first day, you eat an apple that grew on the first day.
- On the second day, you eat an apple that grew on the second day.
- On the third day, you eat an apple that grew on the second day. After this day, the apples that grew on the third day rot.
- On the fourth to the seventh days, you eat apples that grew on the fourth day.
Example 2:

Input: apples = [3,0,0,0,0,2], days = [3,0,0,0,0,2]
Output: 5
Explanation: You can eat 5 apples:
- On the first to the third day you eat apples that grew on the first day.
- Do nothing on the fouth and fifth days.
- On the sixth and seventh days you eat apples that grew on the sixth day.
 

Constraints:

n == apples.length == days.length
1 <= n <= 2 * 104
0 <= apples[i], days[i] <= 2 * 104
days[i] = 0 if and only if apples[i] = 0.



class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        import heapq

        # Min-heap to store apples in the form (expiration_day, apples_count)
        heap = []
        i = 0
        eaten = 0
        n = len(apples)

        while i < n or heap:
            # Remove all the apples that have already rotted
            while heap and heap[0][0] <= i:
                heapq.heappop(heap)

            # If apples grow today, add them to the heap
            if i < n and apples[i] > 0:
                heapq.heappush(heap, (i + days[i], apples[i]))

            # Eat one apple if possible
            if heap:
                # Get the entry with the nearest expiration day
                exp_day, count = heapq.heappop(heap)
                eaten += 1
                # If there are still apples remaining from that batch, push them back with reduced count
                if count > 1:
                    heapq.heappush(heap, (exp_day, count - 1))

            i += 1

        return eaten