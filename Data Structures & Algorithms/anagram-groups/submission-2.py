from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # defaultdict(list) で、キーが存在しなくても自動で空リストを作る
        res = defaultdict(list)
        for  alphabet in strs:
            count = [0] * 26
            for alpha in alphabet:
                count[ord(alpha) - ord('a')] += 1
            res[tuple(count)].append(alphabet)
        return list(res.values())