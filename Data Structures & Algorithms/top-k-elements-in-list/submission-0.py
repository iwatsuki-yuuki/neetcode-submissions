class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = defaultdict(int)

        freq_buckets = [[]for _ in range(len(nums) + 1)]

        for num in nums:
            count_map[num] += 1

        for num, c in count_map.items():
            freq_buckets[c].append(num)

        res = []

        for i in range(len(freq_buckets) -1, 0, -1):
            for num in freq_buckets[i]:
                res.append(num)

                if len(res) == k:
                    return res