class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums = sorted(nums)
        dlina = len(nums)
        return [i for i in range(dlina) if nums[i] == target]
