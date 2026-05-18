class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        my_index = 0
        product = 1
        res = [1] * len(nums) 
        for j in range(len(nums)):
            for i in range(len(nums)):
                if my_index == i:
                    continue
                product *= nums[i] 

            res[my_index] = product
            my_index += 1
            product = 1

        return res