class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement_to_index = dict()
        for i, num in enumerate(nums):
            if num in complement_to_index:
                return [complement_to_index[num], i]
            complement_to_index[target - num] = i
        return []