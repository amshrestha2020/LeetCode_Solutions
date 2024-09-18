You are given an m x n integer matrix grid​​​, where m and n are both even integers, and an integer k.

The matrix is composed of several layers, which is shown in the below image, where each color is its own layer:



A cyclic rotation of the matrix is done by cyclically rotating each layer in the matrix. To cyclically rotate a layer once, each element in the layer will take the place of the adjacent element in the counter-clockwise direction. An example rotation is shown below:


Return the matrix after applying k cyclic rotations to it.

 

Example 1:


Input: grid = [[40,10],[30,20]], k = 1
Output: [[10,20],[40,30]]
Explanation: The figures above represent the grid at every state.
Example 2:


Input: grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], k = 2
Output: [[3,4,8,12],[2,11,10,16],[1,7,6,15],[5,9,13,14]]
Explanation: The figures above represent the grid at every state.
 

Constraints:

m == grid.length
n == grid[i].length
2 <= m, n <= 50
Both m and n are even integers.
1 <= grid[i][j] <= 5000
1 <= k <= 109




class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        
        # Function to extract a layer as a list
        def extract_layer(layer):
            elements = []
            # Top row (left to right)
            for col in range(layer, n - layer):
                elements.append(grid[layer][col])
            # Right column (top to bottom)
            for row in range(layer + 1, m - layer):
                elements.append(grid[row][n - layer - 1])
            # Bottom row (right to left)
            for col in range(n - layer - 2, layer - 1, -1):
                elements.append(grid[m - layer - 1][col])
            # Left column (bottom to top)
            for row in range(m - layer - 2, layer, -1):
                elements.append(grid[row][layer])
            
            return elements
        
        # Function to place the rotated elements back into the layer
        def place_layer(layer, rotated):
            idx = 0
            # Top row (left to right)
            for col in range(layer, n - layer):
                grid[layer][col] = rotated[idx]
                idx += 1
            # Right column (top to bottom)
            for row in range(layer + 1, m - layer):
                grid[row][n - layer - 1] = rotated[idx]
                idx += 1
            # Bottom row (right to left)
            for col in range(n - layer - 2, layer - 1, -1):
                grid[m - layer - 1][col] = rotated[idx]
                idx += 1
            # Left column (bottom to top)
            for row in range(m - layer - 2, layer, -1):
                grid[row][layer] = rotated[idx]
                idx += 1

        # Process each layer
        for layer in range(min(m, n) // 2):
            # Extract the current layer
            elements = extract_layer(layer)
            # Determine the number of rotations, as k can be large
            total_elements = len(elements)
            rotation_steps = k % total_elements
            # Rotate the layer's elements
            rotated = elements[rotation_steps:] + elements[:rotation_steps]
            # Place the rotated elements back into the grid
            place_layer(layer, rotated)
        
        return grid