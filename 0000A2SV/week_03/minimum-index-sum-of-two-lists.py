class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common = set(list1)&set(list2)
        common_map = {}
        for each_word in common:
            common_map[each_word] = [0,0]
        for index,word in enumerate(list1):
            if word in common:
                common_map[word][0] = index
        for index,word in enumerate(list2):
            if word in common:
                common_map[word][1] = index
        min_sum = float('inf')
        for word in common:
            min_sum = min(min_sum, sum(common_map[word]))
        solution = []
        for word in common:
            if min_sum == sum(common_map[word]):
                solution.append(word)
        return solution



