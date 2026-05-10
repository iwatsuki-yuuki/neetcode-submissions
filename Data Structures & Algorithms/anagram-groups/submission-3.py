from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count_list = [0] * 26
            for i in s:
                count_list[ord(i) - ord('a')] += 1
            
            res[tuple(count_list)].append(s)
        return list(res.values())