# DS: Array
# ALGO:
# Time: O(n). Space: O(1)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # The 'answer' array will first be used to store the prefix products.
        # Initialize the array with the correct length.
        answer = [0] * n

        # ------------------
        # 1. Left Pass (Prefix Products)
        # ------------------
        # answer[i] will contain the product of all elements to the left of i.
        # For index 0, there are no elements to the left, so the product is 1.
        answer[0] = 1

        # Iterate from index 1 to n-1
        for i in range(1, n):
            # The product to the left of i is the product to the left of (i-1)
            # multiplied by nums[i-1].
            answer[i] = nums[i - 1] * answer[i - 1]

        # At the end of this loop, answer looks like:
        # nums: [1, 2, 3, 4]
        # answer: [1, 1, 2, 6]  (Prefix products)

        # ------------------
        # 2. Right Pass (Suffix Products and Final Calculation)
        # ------------------
        # R will hold the product of all elements to the right of the current index i.
        R = 1

        # Iterate backward from n-1 down to 0
        for i in range(n - 1, -1, -1):

            # 1. Calculate the final answer[i]:
            # answer[i] currently holds the prefix product (L).
            # R currently holds the suffix product (R).
            # answer[i] = L * R
            answer[i] = answer[i] * R

            # 2. Update R for the next iteration:
            # R needs to include nums[i] for the product calculation of the next index (i-1).
            R = R * nums[i]

        return answer
