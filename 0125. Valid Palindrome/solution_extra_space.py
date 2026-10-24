# DS: String
# ALGO: Two Pointers
# Time: O(n). Space: O(n)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # data cleaning
        alphanumeric = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789"
        s_clean_list = []
        for c in s.lower().strip():
            if c in alphanumeric:
                s_clean_list.append(c)
        if not s_clean_list:
            return True  # empty string is a palindrome
        s_clean = "".join(s_clean_list)

        # check palindrome with two pointers
        left = 0
        right = len(s_clean) - 1
        while left < right:
            if s_clean[left] != s_clean[right]:
                return False
            left += 1
            right -= 1
        return True
