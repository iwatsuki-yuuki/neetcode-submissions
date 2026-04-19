import collections
'''
q = deque()       # 空のdequeを作成
q.append(1)       # [1]
q.append(2)       # [1, 2]
q.appendleft(0)   # [0, 1, 2]
q.pop()           # [0, 1]  → 取り出した値: 2
q.popleft()       # [1]     → 取り出した値: 0
'''
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        # index
        q = collections.deque()
        l = r = 0
        while r < len(nums):
            # dequeが空でないこと確認し、新しい値が末尾より小さければ末尾捨てる
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])   
                l += 1
            r += 1
        return output     
