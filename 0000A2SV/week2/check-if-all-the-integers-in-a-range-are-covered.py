class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        range_end = right
        for each_range in ranges:
            range_end = max(range_end, each_range[1])
        range_array = [0]*(range_end+2)
        for each_range in ranges:
            range_array[each_range[0]] += 1
            range_array[each_range[1]+1] -= 1
        for i in range(1,range_end+2):
            range_array[i] += range_array[i-1]
        for number in range(left,right+1):
            if  range_array[number] < 1:
                return False
        return True

            
