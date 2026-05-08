class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 配列の中身を渡して出現頻度をカウントする
        # kと比べて出現頻度が高いやつから順番に出力する
        res = {}
        for num in nums:
            res[num] = 1 + res.get(num,0)

        return sorted(res, key=res.get, reverse=True)[:k]
