class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x,y = 0,0
        for each_move in moves:
            y += each_move == "U";
            y -= each_move == "D";
            x += each_move == "R";
            x -= each_move == "L";
            
        return x == 0 and y == 0
        