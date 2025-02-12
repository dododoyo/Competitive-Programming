# Problem: Find Duplicate File in System - https://leetcode.com/problems/find-duplicate-file-in-system/

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        unique_contents = defaultdict(list)

        # get file in each folder 
        for path in paths:
            files = path.split(" ")
            root_ = files[0]
            # start from 1 because the 0th 
            # element is the root filename
            for index in range(1,len(files)):
                #get content and file_name
                current_file = files[index]
                finder = 0;

                #get the file_name and the content
                while current_file[finder] != "(":
                    finder += 1

                file_name = current_file[:finder]
                content = current_file[finder:len(current_file)]

                unique_contents[content].append(root_+"/"+file_name)

        return [content for content in unique_contents.values() if  len(content) > 1]