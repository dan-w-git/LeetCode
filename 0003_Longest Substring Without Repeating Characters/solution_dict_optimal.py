# DS: String
# ALGO: Sliding Window
# Time: O(n). Space: O(min(m,n)). m: size of charset, n: length of string
# 2n operations

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        l = 0
        r = 0
        seen = set()
        max_len = 1

        while r < len(s):
            if s[r] in seen:
                max_len = max(max_len, r - l)
                # advance l to duplicated char while cleaning up set
                while s[l] != s[r]:
                    seen.remove(s[l])
                    l += 1
                l += 1
            else:
                seen.add(s[r])

            r += 1

        return max(max_len, r - l)
