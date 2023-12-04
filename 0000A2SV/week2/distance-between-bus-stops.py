class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if destination > start:
            forward_path = sum(distance[start:destination])
            backward_path = sum(distance[destination:])+ sum(distance[:start])
        else:
            forward_path = sum(distance[destination:start])
            backward_path = sum(distance[:destination])+ sum(distance[start:])

        return min(backward_path,forward_path)

        