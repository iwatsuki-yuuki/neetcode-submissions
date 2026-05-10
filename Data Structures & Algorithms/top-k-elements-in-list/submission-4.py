class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for num in nums:
            res[num] = 1 + res.get(num, 0)

        return sorted(res, key=res.get, reverse=True)[:k]