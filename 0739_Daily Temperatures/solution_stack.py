# DS: Stack
# ALGO:
# Time: O(n). Space: O(n)

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # use a stack to store indices of temps lower than previous day
        stack = []
        answer = [0] * len(temperatures)  # initialize every element to 0

        for current_day, current_temp in enumerate(temperatures):
            if current_day == 0:
                stack.append(current_day)
                continue

            # compare current temp with lowest temp in stack
            while stack and current_temp > temperatures[stack[-1]]:
                lowest_temp_day = stack.pop()
                answer[lowest_temp_day] = current_day - lowest_temp_day

            # temps lower than current temp are cleared from stack before current temp is added.
            # stack is non-increasing (monotonic). last index is always for the lowest temp encountered so far
            stack.append(current_day)

        return answer

        # brute force
        # answer = []
        # n = len(temperatures)
        # for i in range(n):
        #     days = 0
        #     for j in range(i + 1, n):
        #         if temperatures[j] > temperatures[i]:
        #             days = j - i
        #             break
        #     answer.append(days)

        # return answer
