# Problem: Time Based Key-Value Store - https://leetcode.com/problems/time-based-key-value-store/

class TimeMap:
    def __init__(self):
        self.time = defaultdict(list)
        self.values = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time[key].append(timestamp)
        self.values[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        index = bisect.bisect(self.time[key], timestamp)
        if index == 0:
            return ''
        return self.values[key][index - 1]