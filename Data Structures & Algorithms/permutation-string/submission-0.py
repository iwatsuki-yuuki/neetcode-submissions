class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)

        if n > m:
            return False
        
        # 比較のために、s1をあらかじめsortしておく
        sorted_s1 = sorted(s1)

        # s2から長さnの部分文字列を順番に取り出すためのループ
        for i in range(m - n + 1):
            sub_s2 = s2[i : i + n]

            if sorted(sub_s2) == sorted_s1:
                return True
        
        return False
        
        