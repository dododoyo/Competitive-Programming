class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        current_can_water = capacity
        total_steps = 0
        for right in range(len(plants)):
            if plants[right] > current_can_water:
                current_can_water = capacity
                total_steps += 2*(right)
            current_can_water -= plants[right]
            total_steps += 1
        return total_steps
                
        