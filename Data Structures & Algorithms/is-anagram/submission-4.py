class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str_set = list(s)
        if len(s)!=len(t):
            return False
        for i in t:
            if i not in str_set:
                return False
            else:
                str_set.remove(i)
        return True