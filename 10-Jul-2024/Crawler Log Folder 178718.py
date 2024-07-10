# Problem: Crawler Log Folder - https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        answer = []
        # we have three options 
        for log in logs:
            if log == "../":
                if answer:
                    answer.pop()
            elif log != "./":answer.append(log)
        return len(answer)

        