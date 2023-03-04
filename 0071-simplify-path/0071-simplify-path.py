class Solution:
    def simplifyPath(self, path: str) -> str:
        simplified = []
        current_word = ""
        
        for character in path+"/":
            if character == "/":
                if current_word == "..":
                    if simplified:
                        simplified.pop()
                elif current_word != "" and current_word != ".":
                    simplified.append(current_word)
                current_word = ""
            else:
                current_word += character
        return "/" + "/".join(simplified)