class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        
        # 部分文字列のスタート地点 (i) を全探索
        for i in range(len(s)):
            count = {} # その部分文字列の中にある文字の数を数える辞書
            max_freq = 0 # 一番多い文字の数
            
            # スタート地点 (i) からゴール地点 (j) を右に伸ばしていく
            for j in range(i, len(s)):
                char = s[j]
                
                # 新しく入ってきた文字をカウントに追加
                count[char] = count.get(char, 0) + 1
                
                # 「一番多い文字の数」を更新
                max_freq = max(max_freq, count[char])
                
                # 今見ている部分文字列の長さ
                current_length = j - i + 1
                
                # (全体の長さ) - (一番多い文字の数) = (置換が必要な文字数)
                # これが k 以下なら、条件クリア！
                if current_length - max_freq <= k:
                    max_length = max(max_length, current_length)
                else:
                    # 置換回数が k を超えてしまったら、これ以上 j を右に伸ばしても
                    # 条件を満たすことは二度とないので、このスタート地点(i)の探索は打ち切る
                    break
                    
        return max_length