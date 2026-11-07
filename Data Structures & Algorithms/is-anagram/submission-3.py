class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        frequencyS = {}
        frequencyT = {}

        for letter in s: 
            if letter in frequencyS:
                frequencyS[letter] = frequencyS[letter] + 1
            else: 
                frequencyS[letter] = 1

        for letter in t:
            if letter in frequencyT:
                frequencyS[letter] = frequencyS[letter] + 1
            else: 
                frequencyT[letter] = 1

        return frequencyS == frequencyT
        