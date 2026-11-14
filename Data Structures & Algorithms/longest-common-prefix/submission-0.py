class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans =[]
        for i in range(len(strs[0])):
            char = strs[0][i]
            for word in strs:
                if i>=len(word) or word[i] != char:
                    return "".join(ans)
            ans.append(char)
        return "".join(ans)