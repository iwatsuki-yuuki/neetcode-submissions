class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # 絶対忘れないソート！
        res = []

        for i in range(len(nums)):
            # 【追加1】1つ目の数字の重複スキップ
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # (ちょっとした小技: もし nums[i] が 0 より大きかったら、もう合計0にはならないので終了してOK)
            if nums[i] > 0:
                break

            left = i + 1
            right = len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum < 0:
                    left += 1
                elif current_sum > 0:
                    right -= 1
                else:
                    # 答えが見つかった！
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # 次の候補を探すために両方動かす
                    left += 1
                    right -= 1
                    
                    # 【追加2】2つ目以降の数字の重複スキップ
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return res