class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 各数値の出現回数を記録するための空の辞書を用意する
        # 例: nums = [1,2,2,3,3,3] なら最終的に {1:1, 2:2, 3:3} になる
        res = {}

        for num in nums:
            # res.get(num, 0) は「numがresに存在すればその値、なければ0」を返す
            # それに1を足してres[num]に代入することで出現回数をカウントする
            #
            # 例) num=2 を初めて見たとき: res.get(2, 0) → 0  なので res[2] = 1 + 0 = 1
            # 例) num=2 を2回目に見たとき: res.get(2, 0) → 1  なので res[2] = 1 + 1 = 2
            res[num] = 1 + res.get(num, 0)

        # sorted(res, ...) は辞書のキー（数値）のリストをソートする
        # key=res.get  → 各キーに対して res.get(num) を呼び出し、出現回数を基準にソートする
        #                key=lambda num: res[num] と同じ意味
        # reverse=True → 出現回数が多い順（降順）に並べる
        #
        # 例: res = {1:1, 2:2, 3:3} なら sorted後 → [3, 2, 1]
        #
        # [:k] → 先頭からk個だけ取り出す = 出現頻度Top Kの要素を返す
        # 例: k=2 なら [3, 2] を返す
        return sorted(res, key=res.get, reverse=True)[:k]