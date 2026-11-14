class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        visited = set()
        data = []
        final = []
        for word in strs:
            data.append(Counter(word))
        for i in range(len(strs)):
            if i in visited:
                continue
            ans = []
            for j in range(len(strs)):
                if j not in visited and data[i]==data[j]:
                    ans.append(strs[j])
                    visited.add(j)
            final.append(ans)
        return final


                    