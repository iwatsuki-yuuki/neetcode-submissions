class Solution:
    def encode(self, strs: List[str]) -> str:
        # 各文字列を「長さ + '#' + 本体」の形にして連結する
        # 例: ["neet","code"] → "4#neet4#code"
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0  # 読み取りカーソル
        while i < len(s):
            # 1) '#' の位置 j を探す。s[i:j] が長さの数字(複数桁OK)
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])

            # 2) '#' の次から length 文字を切り出して1要素とする
            i = j + 1
            j = i + length
            res.append(s[i:j])

            # 3) 次のブロックの先頭へカーソルを移動
            i = j
        return res