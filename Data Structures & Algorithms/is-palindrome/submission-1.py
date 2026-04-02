class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            # 1. 左の指を、文字が見つかるまで進める
            while left < right and not s[left].isalnum():
                left += 1
                
            # 2. 右の指を、文字が見つかるまで左へ進める（ここを書いてみましょう！）
            while left < right and not s[right].isalnum():
                right -= 1
                
            # 3. 両方の指が文字を指しているので、小文字にして比較する
            if s[left].lower() != s[right].lower():
                return False  # 違ったら即アウト！
            
            # 4. 同じ文字だったら、次の文字へ指を進める
            left += 1
            right -= 1

        # すべてのチェックをすり抜けたら、それは回文！
        return True