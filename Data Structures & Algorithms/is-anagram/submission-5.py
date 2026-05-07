class Solution:
        # 時間計算量: O(n + m)
        #   s を全部ループ（n回）+ t を全部ループ（m回）するため
        #   処理回数が文字列の長さに比例する
        # 空間計算量: O(1)
        #   辞書のキーは文字の種類 = 最大26種類（英小文字のみの制約）
        #   n や m がどれだけ大きくなっても辞書サイズは最大26で固定
        #   入力サイズに依存しない定数 → O(定数) = O(1)
    def isAnagram(self, s: str, t: str) -> bool:
        # 長さが違う場合は即座にFalse
        if len(s) != len(t):
            return False
        # sとtそれぞれの文字の出現頻度を記録する辞書
        # ハッシュマップ
        countS, countT = {}, {}

        # 2つの文字列を同時にループしてカウント
        for i in range(len(s)):
            # s[i]の出現回数を+1（まだキーがなければ0として扱う）
            countS[s[i]] = 1 + countS.get(s[i],0)
            # t[i]の出現回数を+1
            countT[t[i]] = 1 + countT.get(t[i],0)

# 二つの辞書が完全に一致すれば同じ文字、同じ頻度
        return countS == countT