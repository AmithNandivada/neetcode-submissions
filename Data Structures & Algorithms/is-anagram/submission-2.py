class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = "".join(sorted(s))
        sorted_t = "".join(sorted(t))

        if sorted_s == sorted_t:
            return True
        return False
        # if len(s) != len(t):
        #     return False
        
        # s_chars = {}
        # t_chars = {}

        # for i in s:
        #     if i in s_chars:
        #         s_chars[i] += 1
        #     else:
        #         s_chars[i] = 1

        # for i in t:
        #     if i in t_chars:
        #         t_chars[i] += 1
        #     else:
        #         t_chars[i] = 1

        # return s_chars == t_chars
            