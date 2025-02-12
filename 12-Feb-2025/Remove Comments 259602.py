# Problem: Remove Comments - https://leetcode.com/problems/remove-comments/

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        # source => array of strings 

        inside_block_comment = False
        ans = []
        for line in source:
            i = 0

            if (not inside_block_comment):
                newline = []

            # when parsing line we have four possibilities 
            while i < len(line):
                # start of block comment
                if line[i:i+2] == '/*' and (not inside_block_comment):
                    inside_block_comment = True
                    i += 1
                
                # end of block comment
                elif line[i:i+2] == '*/' and inside_block_comment:
                    inside_block_comment = False
                    i += 1

                # inside line comment 
                elif (not inside_block_comment) and line[i:i+2] == '//':
                    break
                
                # code 
                elif (not inside_block_comment):
                    newline.append(line[i])
                
                i += 1

            if newline and (not inside_block_comment):

                ans.append("".join(newline))

        return ans