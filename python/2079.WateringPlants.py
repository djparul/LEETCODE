# 2079.WateringPlants.py 
#  https://leetcode.com/problems/watering-plants
class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 1 
        current_capacity = capacity
        for i in range(len(plants) - 1):
            current_capacity -= plants[i]
            if current_capacity < plants[i+1]:
                steps += (i + 1) * 2 + 1
                current_capacity = capacity
            else:
                steps += 1
        return steps