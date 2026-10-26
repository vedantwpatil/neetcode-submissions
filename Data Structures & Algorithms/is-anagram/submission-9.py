class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False

        letter_frequency_s = {}
        letter_frequency_t = {}

        for i in range(len(s)): 
            letter_s = s[i]
            letter_t = t[i]
            letter_frequency_s[letter_s] = letter_frequency_s.get(letter_s, 0) + 1 
            letter_frequency_t[letter_t] = letter_frequency_t.get(letter_t, 0) + 1 

        return letter_frequency_s == letter_frequency_t
        