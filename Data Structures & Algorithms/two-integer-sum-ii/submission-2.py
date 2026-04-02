class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 変数にtargetから引いた値を格納し、辞書で探すアルゴリズムを実装する
        # 検索をかけるのはキーなので、キーに差分の値を入れる
        # 値はnumbersのインデックス番号を入れる
        dic = defaultdict(int)
        for i, number in enumerate(numbers):
            number_minus = target - number
            dic[number_minus] = i
        # dict = {2: 0, 1: 1. 0: 2, -1: 3}
        for i in range(len(numbers)):
            # number[0] = 1でdictの２番目のキーが1で見つかる
            if numbers[i] in dic:
                return [i + 1, dic[numbers[i]] + 1]