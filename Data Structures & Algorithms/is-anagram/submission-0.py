class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        frequencyS = [0] * len(s)
        frequencyT = [0] * len(t)

        for letter in s: 
            frequencyS[ord(letter)] = frequencyS[ord(letter)] + 1
        for letter in t:
            frequencyT[ord(letter)] = frequencyT[ord(letter)] + 1

        return frequencyS == frequencyT
        