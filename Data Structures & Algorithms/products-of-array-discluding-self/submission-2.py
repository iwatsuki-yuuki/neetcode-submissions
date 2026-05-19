class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 答え = (左側の積) × (右側の積) を 2パスで構築する
        # 時間 O(n) / 追加メモリ O(1)

        # 掛け算なので単位元 1 で初期化
        res = [1] * len(nums)

        # 1パス目: res[i] に「i より左の積」を入れる
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix          # 先に書き込む（nums[i] を含めない）
            prefix *= nums[i]        # その後で更新

        # 2パス目: 右から走査して「i より右の積」を掛け合わせる
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix        # 先に掛ける（nums[i] を含めない）
            postfix *= nums[i]       # その後で更新

        return res