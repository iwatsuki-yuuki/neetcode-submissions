class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        count_list = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        

        for key, value in count.items():
            count_list[value].append(key)

        res = []

        for i in range(len(count_list) - 1, 0, -1):
            for number in count_list[i]:
                res.append(number)
                if len(res) == k:
                    return res