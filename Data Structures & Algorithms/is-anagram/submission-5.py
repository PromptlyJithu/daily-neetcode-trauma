class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str_list = Counter(s)
        if len(s)!=len(t):
            return False
        for i in t:
            if str_list[i] == 0:
                return False
            else:
                str_list[i] -= 1
        return True