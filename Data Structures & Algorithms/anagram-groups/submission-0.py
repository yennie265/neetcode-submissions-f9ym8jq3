class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """Solution 1
        res = defaultdict(list) #mapping charCount to list of Anagrams
        for s in strs:
            count = [0] * 26 #a ... z

            for c in s:
                count[ord(c) - ord ("a")] += 1 

            res[tuple(count)].append(s)

        return list(res.values())"""

        res = defaultdict(list)
        for s in strs:
            sortedS = ' '.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())