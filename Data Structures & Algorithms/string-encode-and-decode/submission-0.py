class Solution:
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        res = []
        for string in strs:
            length = len(string)
            res.append(str(length) + "#" + string)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            length = 0
            while s[i].isdigit():
                length = length * 10 + int(s[i])
                i += 1
            i += 1 # for skipping hash #
            decoded_str = s[i : i + length]
            res.append(decoded_str)
            i += length
        return res
