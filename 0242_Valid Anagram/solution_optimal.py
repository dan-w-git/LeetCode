# DS: Array, Dictionary / HashMap
# ALGO:
# Time: O(n), Space: O(n)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dict = {}

        for l in s:
            dict[l] = dict.get(l, 0) + 1

        for m in t:
            if m not in dict:
                return False

            dict[m] -= 1
            if dict[m] < 0:
                return False

        return True
