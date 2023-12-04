class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps,can_water = 0,capacity
        for current_position in range(len(plants)):
            if plants[current_position] > can_water:
                steps += 2*current_position
                can_water = capacity
            steps += 1
            can_water -= plants[current_position]
        return steps
