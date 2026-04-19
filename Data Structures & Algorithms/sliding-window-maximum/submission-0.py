class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # ウィンドウの左端と右端のインデックスの初期値
        # k = 3で考えてみる
        left = 0
        right = left + k - 1   
        # 最大値を格納するリスト
        big_num = []
        for i in range(len(nums) - k + 1):         
            window = nums[left:right + 1]
            big_num.append(max(window))
            left += 1
            right += 1
    
        return big_num

