# DS: Array
# ALGO: Sorting
# Time: O(nlogn). Space: O(n)
# More intuitive than stack approach

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # calculate hours to target for each car
        n = len(position)
        car_data = sorted(zip(position, speed), reverse=True)
        time_to_target = [(target - pos) / spd for pos, spd in car_data]

        # iterate over cars to check whether adjacent cars will catch up and form a fleet.
        fleet_num = 1  # at least one fleet
        longest_to_target_in_fleet = time_to_target[0]
        for i in range(1, n):
            if time_to_target[i] > longest_to_target_in_fleet:
                # current car is further away from target than slowest car in fleet
                # because array is sorted by descending position.
                # if current car is projected to reach target later than latest car in fleet to reach target,
                # it won't catch up and join the fleet, and will form a separate fleet
                fleet_num += 1
                longest_to_target_in_fleet = time_to_target[i]
            # if current car joins a fleet, it's projected to reach target faster than
            # existing latest car in fleet to reach target. no need to update longest_to_target_in_fleet

        return fleet_num
