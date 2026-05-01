class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_dict = {}
        for i in range(len(nums)):
            if num_dict.get(nums[i], 0):
                return True
            num_dict[nums[i]] = 1
        return False


