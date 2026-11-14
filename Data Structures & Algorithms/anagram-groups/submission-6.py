class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data=[]
        for word in strs:
            data.append(tuple(sorted(word)))
        group={}
        for i in range(len(strs)):
            if data[i] not in group:
                group[data[i]] =[]
            group[data[i]].append(strs[i])
        return list(group.values())

                    