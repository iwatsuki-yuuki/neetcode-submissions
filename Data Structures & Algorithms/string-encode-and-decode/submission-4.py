class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        # 例: ["Hello", "World"] → "5#Hello5#World"
        return res
        
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            # i から始めて '#' の位置 j を探す
            j = i
            while s[j] != '#':
                j += 1
            # i 〜 j の手前までが数字(長さ)
            length = int(s[i:j])
            # '#' の次から length 文字が単語
            word = s[j+1 : j+1+length]
            res.append(word)
            # 次の単語の先頭へジャンプ
            i = j + 1 + length
        return res
