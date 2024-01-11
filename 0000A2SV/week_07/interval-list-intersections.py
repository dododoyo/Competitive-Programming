class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        # use two pointers located at each list's begining 
        # to track if there is an intersection
        solution = []
        first_pointer,second_pointer = 0,0
        while first_pointer < len(firstList) and second_pointer < len(secondList):
            if firstList[first_pointer][0] >= secondList[second_pointer][0]:
                destination = min(secondList[second_pointer][1],firstList[first_pointer][1])
                if destination >= firstList[first_pointer][0]:
                    solution.append([firstList[first_pointer][0],destination])
            else:
                destination = min(secondList[second_pointer][1],firstList[first_pointer][1])
                if destination >= secondList[second_pointer][0]:
                    solution.append([secondList[second_pointer][0],destination])

            if secondList[second_pointer][1] > firstList[first_pointer][1]:
                first_pointer += 1
            else: 
                second_pointer += 1
        return solution