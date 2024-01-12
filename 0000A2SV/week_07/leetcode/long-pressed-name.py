class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        name_pointer = 0
        for typed_pointer in range(len(typed)):
            if name_pointer < len(name) and name[name_pointer] == typed[typed_pointer]:
                name_pointer += 1
            elif typed_pointer == 0 or typed[typed_pointer] != typed[typed_pointer-1]:
                return False
        return len(name) == name_pointer
        