class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        returnHash = collections.defaultdict(list)

        for word in strs:
            count = [0] * 26
            
            for letter in word:
                count[ord(letter) - ord("a")] += 1
            returnHash[tuple(count)].append(word)

        return list(returnHash.values())