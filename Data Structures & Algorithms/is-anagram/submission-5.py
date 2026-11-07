class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = {}
        countT = {}

        if len(s) != len(t):
            return False 

        for i in range(len(s)):
            if s[i] in countS:
                countS[i] = countS.get(s[i]) + 1 
            else: 
                countS[i] = 1
            if t[i] in countT:
                countT[i] = countT.get(t[i]) + 1 
            else: 
                countT[i] = 1
        return countT == countS 
        