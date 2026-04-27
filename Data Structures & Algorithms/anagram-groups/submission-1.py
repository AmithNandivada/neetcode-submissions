from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            sorted_key_word = "".join(sorted(word))
            groups[sorted_key_word].append(word)

        return list(groups.values())