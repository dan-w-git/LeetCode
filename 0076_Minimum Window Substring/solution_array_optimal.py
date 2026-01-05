# DS: String
# ALGO: Sliding Window
# Time: O(m + n). Space: O(m + n)

"""
Start with the Array: If the constraints say "lowercase English letters" or "ASCII," tell them you'll use an array for better performance and cache locality.

Pivot to Hash Map: Mention that if the character set were unknown or extremely large (like UTF-8), you would switch to a dict to remain memory efficient.
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""

        # Use 128 to cover all standard ASCII (covers 'A'-'Z' and 'a'-'z')
        # There's a gap in the ASCII table between uppercase 'Z' (90) and lowercase 'a' (97)
        target_counts = [0] * 128
        window_counts = [0] * 128

        # Count unique characters needed in t
        required_unique = 0
        for char in t:
            if target_counts[ord(char)] == 0:
                required_unique += 1
            target_counts[ord(char)] += 1

        l, r = 0, 0
        formed = 0
        min_len = float("inf")
        ans_indices = (-1, -1)

        while r < len(s):
            # 1. Expand the window by adding character at r
            char_r = ord(s[r])
            window_counts[char_r] += 1

            # If this character completes the required count for this specific letter
            if target_counts[char_r] > 0 and window_counts[char_r] == target_counts[char_r]:
                formed += 1

            # 2. Try to shrink the window from the left
            while l <= r and formed == required_unique:
                # Update the best window found so far
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    ans_indices = (l, r)

                char_l = ord(s[l])
                # Character leaving the window
                window_counts[char_l] -= 1

                # If removing s[l] breaks the "validity" of our window
                if target_counts[char_l] > 0 and window_counts[char_l] < target_counts[char_l]:
                    formed -= 1

                l += 1  # Shrink

            r += 1  # Expand

        start, end = ans_indices
        return s[start: end + 1] if min_len != float("inf") else ""
