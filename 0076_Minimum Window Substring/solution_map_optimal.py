# DS: String
# ALGO: Sliding Window
# Time: O(m + n). Space: O(m + n)

from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        # Dictionary which keeps a count of all the unique characters in t.
        dict_t = Counter(t)
        required = len(dict_t)

        # Left and Right pointer
        l, r = 0, 0

        # formed is used to keep track of how many unique characters in t
        # are present in the current window in its required frequency.
        formed = 0
        window_counts = {}

        # ans tuple of the form (window length, left, right)
        ans = float("inf"), None, None

        while r < len(s):
            # Add character from the right to the window
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1

            # If the frequency of the current character matches the desired count in t
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1

            # Try and contract the window till the point where it ceases to be 'desirable'.
            while l <= r and formed == required:
                character = s[l]

                # Save the smallest window until now.
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                # The character at the position pointed by the `left` pointer is no longer a part of the window.
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1

                # Move the left pointer ahead, this helps to look for a new window.
                l += 1

            # Keep expanding the window by moving the right pointer
            r += 1

        return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]
