class Robot:
    def __init__(self, width: int, height: int):
        self.width,self.height = width,height
        # from the perimeter we are decreasing 4 
        # because we want to get the number of cells
        self.loop_perimeter,self.steps  = 2*(width + height)-4,0

    def helper(self):
        if self.steps == 0:
            return (0,0,"East")
        # since we are going in a loop we can use 
        # the number of steps the robot has taken 
        # to calculate it's current position and direction

        position = (self.steps-1)%self.loop_perimeter + 1
        # Robot is in the lower row
        if position < self.width:
            return (position, 0, "East")
        # Robot is in the right-most column
        if position < self.width-1+self.height:
            return (self.width-1, position-(self.width-1), "North")
        # Robot is in the top row
        if position < self.width-1+self.height-1+self.width:
            return ((self.width-1)*2+self.height-1 - position, self.height-1, "West")
        # Robot is in the left-most column
        else:
            return ( 0, self.loop_perimeter-position, "South" )
    def step(self, num: int) -> None:
        self.steps += num

    def getPos(self) -> List[int]:
        return self.helper()[:2]

    def getDir(self) -> str:
        return self.helper()[2]

        
# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()