# DS: Array, Frozenset
# ALGO: Hashing
# time: O(n * m), space: O(n + m)
# n: number of strings, m: number of letters in each string

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # store hash and groups of str in master dict. key: hash of occurrence dict, value: list of anagrams
        master_dict = {}

        # count letter occurrences for each str; store in dict
        for s in strs:
            occurrence_dict = {}
            for l in s:
                occurrence_dict[l] = occurrence_dict.get(l, 0) + 1

            # create key from hashable set
            key = hash(frozenset(occurrence_dict.items()))
            if key not in master_dict:
                master_dict[key] = []
            master_dict[key].append(s)

        return list(master_dict.values())
