# DS: String
# ALGO: Sliding Window
# Time: O(n). Space: O(m). n: len(s), m: size of charset (26)

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        freq = {}
        l = 0
        max_freq = 0

        for r in range(len(s)):
            if s[r] in freq:
                freq[s[r]] += 1
            else:
                freq[s[r]] = 1

            # track frequency of most frequent char
            # Since we are looking for the longest substring, we only care when max_f increases.
            # A smaller max_f would never produce a result better than what we've already found.
            max_freq = max(max_freq, freq[s[r]])

            # if number of chars other than the most frequent char can't be all changed to most frequent char,
            # current window is invalid. shrink window by advancing left pointer
            while (r - l + 1) - max_freq > k:
                freq[s[l]] -= 1
                l += 1

            # result = max(result, r - l + 1). simplified because window size never decreases
            # (r - l + 1) > k + max_freq. max_freq never decreases, so (r - l + 1) never decreases
            result = r - l + 1

        return result
