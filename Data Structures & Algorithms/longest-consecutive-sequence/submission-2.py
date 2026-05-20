class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 配列をsetに変換 → 存在チェックがO(1)になり、重複も自動で除去される
        num_set = set(nums)
        # 最長の連続シーケンス長を記録する変数（空配列でも0を返せるよう0で初期化）
        longest = 0

        # setの各要素について順番にチェック
        for num in num_set:
            # num - 1 がsetに無い場合のみ、numは「シーケンスの開始点」
            # （開始点以外から数えるのは無駄なのでスキップ → O(n)を実現するキモ）
            if num - 1 not in num_set:
                # 開始点 num 自身で長さ1からカウントスタート
                length = 1
                # num+1, num+2, ... と連続する数がsetにある限り長さを伸ばす
                while num + length in num_set:
                    length += 1
                # これまでの最長と比較して、大きい方を保持
                longest = max(longest, length)

        # 最終的な最長シーケンス長を返す
        return longest


# ===== 計算量 =====
# 時間計算量: O(n)
#   - forとwhileがネストしているが、whileは「開始点」からしか実行されないため、
#     各要素は最大でも2回しか訪問されない（合計でおよそ2n回の操作）
# 空間計算量: O(n)
#   - num_set に最大 n 個の要素を格納する