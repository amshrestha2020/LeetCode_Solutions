In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino. (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.

Return the minimum number of rotations so that all the values in tops are the same, or all the values in bottoms are the same.

If it cannot be done, return -1.

 

Example 1:


Input: tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]
Output: 2
Explanation: 
The first figure represents the dominoes as given by tops and bottoms: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.
Example 2:

Input: tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]
Output: -1
Explanation: 
In this case, it is not possible to rotate the dominoes to make one row of values equal.
 

Constraints:

2 <= tops.length <= 2 * 104
bottoms.length == tops.length
1 <= tops[i], bottoms[i] <= 6





class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def check(x):
            """
            Return min number of rotations 
            if one could make all elements in A or B equal to x.
            Else return -1.
            """
            # how many rotations should be done
            # to have all elements in A equal to x
            # and to have all elements in B equal to x
            rotations_a = rotations_b = 0
            for i in range(n):
                # rotations coudn't be done
                if tops[i] != x and bottoms[i] != x:
                    return -1
                # A[i] != x and B[i] == x
                elif tops[i] != x:
                    rotations_a += 1
                # A[i] == x and B[i] != x
                elif bottoms[i] != x:
                    rotations_b += 1
            # min number of rotations to have all
            # elements equal to x in A or B
            return min(rotations_a, rotations_b)

        n = len(tops)
        rotations = check(tops[0]) 
        # If one could make all elements in A or B equal to A[0]
        if rotations != -1 or tops[0] == bottoms[0]:
            return rotations 
        # If one could make all elements in A or B equal to B[0]
        else:
            return check(bottoms[0])
