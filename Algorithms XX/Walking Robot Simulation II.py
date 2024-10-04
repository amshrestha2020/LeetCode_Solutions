A width x height grid is on an XY-plane with the bottom-left cell at (0, 0) and the top-right cell at (width - 1, height - 1). The grid is aligned with the four cardinal directions ("North", "East", "South", and "West"). A robot is initially at cell (0, 0) facing direction "East".

The robot can be instructed to move for a specific number of steps. For each step, it does the following.

Attempts to move forward one cell in the direction it is facing.
If the cell the robot is moving to is out of bounds, the robot instead turns 90 degrees counterclockwise and retries the step.
After the robot finishes moving the number of steps required, it stops and awaits the next instruction.

Implement the Robot class:

Robot(int width, int height) Initializes the width x height grid with the robot at (0, 0) facing "East".
void step(int num) Instructs the robot to move forward num steps.
int[] getPos() Returns the current cell the robot is at, as an array of length 2, [x, y].
String getDir() Returns the current direction of the robot, "North", "East", "South", or "West".
 

Example 1:

example-1
Input
["Robot", "step", "step", "getPos", "getDir", "step", "step", "step", "getPos", "getDir"]
[[6, 3], [2], [2], [], [], [2], [1], [4], [], []]
Output
[null, null, null, [4, 0], "East", null, null, null, [1, 2], "West"]

Explanation
Robot robot = new Robot(6, 3); // Initialize the grid and the robot at (0, 0) facing East.
robot.step(2);  // It moves two steps East to (2, 0), and faces East.
robot.step(2);  // It moves two steps East to (4, 0), and faces East.
robot.getPos(); // return [4, 0]
robot.getDir(); // return "East"
robot.step(2);  // It moves one step East to (5, 0), and faces East.
                // Moving the next step East would be out of bounds, so it turns and faces North.
                // Then, it moves one step North to (5, 1), and faces North.
robot.step(1);  // It moves one step North to (5, 2), and faces North (not West).
robot.step(4);  // Moving the next step North would be out of bounds, so it turns and faces West.
                // Then, it moves four steps West to (1, 2), and faces West.
robot.getPos(); // return [1, 2]
robot.getDir(); // return "West"

 

Constraints:

2 <= width, height <= 100
1 <= num <= 105
At most 104 calls in total will be made to step, getPos, and getDir.




class Robot:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.dirs = ["East", "North", "West", "South"]

        # Initialize a single dimension list of [x, y, direction] of grid's outer rim
        self.a = []
        for x in range(self.width):
            self.a.append([x, 0, 0])        # go East
        for y in range(1, self.height):
            self.a.append([self.width - 1, y, 1])    # go North
        for x in range(self.width - 2, -1, -1):
            self.a.append([x, self.height - 1, 2])    # go West
        for y in range(self.height - 2, 0, -1):
            self.a.append([0, y, 3])        # go South

        self.i = 0  # Current position index

    def step(self, num: int) -> None:
        self.i = (self.i + num) % len(self.a)  # mod to simulate cycle/circle
        if self.i == 0:  # once moved, direction becomes South for (0,0)
            self.a[0][2] = 3  

    def getPos(self) -> list[int]:
        return self.a[self.i][:2]  # Return the first two elements - x & y

    def getDir(self) -> str:
        return self.dirs[self.a[self.i][2]]
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()