class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # ハッシュマップを活用
        # 時間計算量: O(n)  ← 配列を1回だけ走査するだけ、空間計算量: O(n)  ← ハッシュマップに最大 n 個の要素を格納
        
        # 過去に見た要素を記録するハッシュマップ
        # キー: 要素の値, バリュー: そのインデックス
        # 例) nums[0] = 2 なら → {2: 0} と記録
        prevMap = {}

        # enumerate で インデックス i と 値 n を同時に取り出す
        for i, n in enumerate(nums):
            # n + diff == targetになるdiffを探したい
            diff = target - n

            # diffがすでにprevMapにあるのか確認→存在した場合過去のループで見た要素が今の要素とペアになる
            if diff in prevMap:
                return [prevMap[diff], i]

            # ペアがまだ見つかっていない場合、現在の要素をマップに記録して次へ
            # ※ 重要：この追加は「チェックの後」に行う
            #    理由：チェックの前に追加してしまうと、
            #          target = 6, n = 3 のとき diff = 3 となり
            #          自分自身（同じインデックス）をペアとして誤検出するバグが起きる
            prevMap[n] = i

        # 問題の制約上「必ず1つ答えが存在する」ので、ここには到達しない
        return []



