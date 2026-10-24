# DS: Array
# ALGO: Pointer Manipulation
# Time: O(n). Space O(1)

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        hottest = 0

        # iterate backwards
        for current_day in range(n - 1, -1, -1):
            current_temp = temperatures[current_day]

            # if we know there is no warmer day after current day,
            # don't update answer (will be 0 for that day) and skip to next iteration
            if current_temp >= hottest:
                hottest = current_temp
                continue

            # keep skipping days to a warmer day,
            # leveraging skipped days (days to wait) from answer
            # use days variable to record skipped days (days to wait)
            days = 1  # start checking from 1 day after current day
            while current_temp >= temperatures[current_day + days]:
                days += answer[current_day + days]

            # when exiting while loop, a warmer day is found
            answer[current_day] = days

        return answer
