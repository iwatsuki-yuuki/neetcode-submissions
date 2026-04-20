class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # ハッシュマップを活用する
        close_to_open = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for c in s:
            # 閉じ括弧の時の条件分岐
            if c in close_to_open:
                # 対応するかっこがあるのか確認する
                if stack and stack[-1] == close_to_open[c]:
                    stack.pop()
                else:
                    return False

            # 開き括弧はスタックに積む
            else: stack.append(c)

        return True if not stack else False

        
