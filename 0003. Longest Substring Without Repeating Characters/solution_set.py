# DS: String
# ALGO: Sliding Window
# Time: O(n). Space: O(min(m,n)). m: size of charset, n: length of string
# n operations

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        # charToNextIndex stores the index after a character for left pointer to jump to when duplicate is encountered
        charToNextIndex = {}

        i = 0
        for j in range(n):
            if s[j] in charToNextIndex:
                # left pointer jumps right after first occurrence of duplicated char
                # max ensures left pointer doesn't jump backward. e.g. abba
                i = max(charToNextIndex[s[j]], i)

            ans = max(ans, j - i + 1)
            charToNextIndex[s[j]] = j + 1

        return ans
