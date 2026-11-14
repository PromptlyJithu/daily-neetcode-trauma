class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = Counter(nums)
        return int(ans.most_common(1)[0][0])