class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # 記号と数値で場合わけ
        # リストの初期化
        array = []
        total = 0

        for i in range(len(tokens)):
            if tokens[i] not in ['+', '-', '*', '/']:
                array.append(int(tokens[i]))
            else:
                # +の時
                if tokens[i] == '+':
                    total = array[-2] + array[-1]
                    array.pop()
                    array.pop()
                    array.append(total)
                    total = 0

                # マイナスの時
                if tokens[i] == '-':
                    total = array[-2] - array[-1]
                    array.pop()
                    array.pop()
                    array.append(total)
                    total = 0

                # 掛け算の時
                if tokens[i] == '*':
                    total = array[-2] * array[-1]
                    array.pop()
                    array.pop()
                    array.append(total)
                    total = 0

                # 割り算の時
                if tokens[i] == '/':
                    total = int(array[-2] / array[-1])
                    print(total, array[-2], array[-1])
                    array.pop()
                    array.pop()
                    array.append(total)
                    total = 0                  
                
        return array[0]