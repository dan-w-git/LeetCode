# DS: String
# ALGO: Sliding Window
# Time: O(n2). Space: O(1)

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False

        # Frequency maps for s1 and the first window of s2
        s1_counts, s2_counts = [0] * 26, [0] * 26
        for i in range(n1):
            s1_counts[ord(s1[i]) - ord('a')] += 1
            s2_counts[ord(s2[i]) - ord('a')] += 1

        # number of letters with correct frequencies between s1 and sliding window of s2
        matches = 0
        for j in range(26):
            if s1_counts[j] == s2_counts[j]:
                matches += 1

        if matches == 26:
            return True

        # slide window
        for k in range(n2 - n1):
            if matches == 26:
                return True

            # char entering window from right
            r = ord(s2[k + n1]) - ord('a')
            s2_counts[r] += 1
            if s2_counts[r] == s1_counts[r]:
                matches += 1
            elif s2_counts[r] == s1_counts[r] + 1:
                # used to match but no longer matches after char entering window
                matches -= 1

            # char leaving window from left
            l = ord(s2[k]) - ord('a')
            s2_counts[l] -= 1
            if s2_counts[l] == s1_counts[l]:
                matches += 1
            elif s2_counts[l] == s1_counts[l] - 1:
                matches -= 1

        return matches == 26
