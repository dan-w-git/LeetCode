# DS: Array, Stack
# ALGO: Sorting
# Time: O(nlogn). Space: O(n)
# Less intuitive than array traversal

class Solution(object):
    def carFleet(self, target, position, speed):
        """
        Calculates the number of car fleets that arrive at the destination.
        A car forms a fleet with the one ahead if it takes less or equal time to reach the target.
        """

        # 1. Combine position and speed, and sort by starting position (ascending).
        # This ensures we process cars from the furthest (0) to the closest (target).
        car_data = sorted(zip(position, speed))

        # 2. Calculate the time each car takes to reach the target.
        # time = distance / speed = (target - position) / speed
        time_to_target = [(target - pos) / spd for pos, spd in car_data]
        # time_to_target = [(target - pos) / float(spd) for pos, spd in car_data] # Python 2

        # We will use this list as a 'stack' and process it from the car closest to target.
        # This car is the *last* element in the list.

        fleet_count = 0

        # 3. Process the cars (times) from closest to furthest.
        # We stop when only one car is left, which is handled after the loop.
        while len(time_to_target) > 1:

            # time_ahead: The time the car/fleet closest to the target takes.
            time_ahead = time_to_target.pop()

            # time_behind: The time the next car (the one behind) takes.
            time_behind = time_to_target[-1]

            # Key Logic:
            if time_ahead < time_behind:
                # If the car/fleet ahead (time_ahead) arrives SOONER than the car behind,
                # the car behind CANNOT catch up and forms a new, separate fleet.
                fleet_count += 1

            else:
                # If the car behind arrives AT THE SAME TIME or SOONER (time_ahead >= time_behind),
                # it catches up to the one ahead, and they form a single fleet.
                # The combined fleet's arrival time is determined by the *later* of the two
                # (which is time_ahead, since the car behind would have caught up to it).
                # We update the time of the car behind to reflect the fleet's arrival time.
                time_to_target[-1] = time_ahead

        # 4. Count the final fleet.
        # If the list is not empty (i.e., bool(time_to_target) is True),
        # the remaining element is the final, uncounted fleet.
        return fleet_count + bool(time_to_target)
