class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        # instead of going from 1 to target 
        # got from target to 1
        moves = 0
        while target > 1:
            # if the current target is even -> half it !
            # because that is the best way to reach to 1
            if target%2 == 0 and maxDoubles > 0:
                target //= 2
                maxDoubles -= 1
                moves += 1

            # if it is odd 
            else:
                # we either can use maxDouble after decreasing 
                # by one or use all our decrements
                if maxDoubles != 0:
                    target -= 1
                    moves += 1
                else:
                    moves += target-1
                    break

        return moves

