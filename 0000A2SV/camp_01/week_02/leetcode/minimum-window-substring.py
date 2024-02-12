class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_map,window_map = Counter(t),defaultdict(int)
        characters_needed,valid_window_characters = len(t_map),0
        solution_length,solution_pointers = len(s)+1,[-1,-1]
        left = 0

        for right in range(len(s)):
            window_map[s[right]] += 1
            if (s[right] in t_map) and (t_map[s[right]] == window_map[s[right]]):
                valid_window_characters += 1
            while valid_window_characters == characters_needed:
                current_length = right-left+1
                if solution_length > current_length:
                    solution_pointers,solution_length = [left,right],current_length
                
                # remove the left character from window 
                # to shrink window size

                window_map[s[left]] -= 1
                # if the decreased value is a valid charcter
                # and when we decreased it it became less than
                # what it should be we no longer have a valid window
                if (s[left] in t_map) and window_map[s[left]] < t_map[s[left]]:
                    valid_window_characters -= 1

                # decrease window size
                left += 1

        return s[solution_pointers[0]:solution_pointers[1]+1] if solution_length != len(s)+1 else ""

        