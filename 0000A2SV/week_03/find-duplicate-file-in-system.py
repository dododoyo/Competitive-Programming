class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        unique_contents = {}

        # get file in each folder 
        for path in paths:
            files = path.split(" ")
            for index in range(1,len(files)):
                #get content and file_name
                finder = 0;

                #get the file_name and the content
                while files[index][finder] != "(":
                    finder += 1
                file_name = files[index][:finder]
                content = files[index][finder:len(files[index])]

                #add each the filename to each unique contents array 
                if content in unique_contents:
                    unique_contents[content].append(files[0]+"/"+file_name)
                else:
                    unique_contents[content] =[files[0]+"/"+file_name]  
        return [content for content in unique_contents.values() if  len(content) != 1]
        