class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        solution = [" "]*(len(s)+len(spaces))
        solution_index,spaces_index = 0,0
        for character_index in range(len(s)):
            if spaces_index < len(spaces) and character_index == spaces[spaces_index]:
                spaces_index += 1
                solution_index+=1
            solution[solution_index] = s[character_index]
            solution_index += 1
        return "".join(solution)