class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a=0
        for i in range(len(nums)):
            for j in range(a,len(nums)):
                if i!=j:
                    if nums[i] + nums[j] == target:
                        return[i,j]
            a+=1
                    