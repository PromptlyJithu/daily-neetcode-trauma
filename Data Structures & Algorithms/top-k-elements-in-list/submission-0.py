class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num=Counter(nums)
        
        pair = num.most_common()
        ans=[]
        i=0
        while i<k:
            ans.append(pair[i][0])
            i+=1
        return ans