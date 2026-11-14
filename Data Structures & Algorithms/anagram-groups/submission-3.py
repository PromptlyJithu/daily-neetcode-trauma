class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = list(strs)
        data = []
        final = []
        for word in strs:
            data.append(Counter(word))
        for i in range(len(strs)):
            ans=[]
            for j in range(i, len(strs)):
                if strs[j] in temp:
                    if data[i] == data[j]:
                        ans.append(strs[j])
                        temp.remove(strs[j])
            if ans != []:
                final.append(ans)
        return final



                    