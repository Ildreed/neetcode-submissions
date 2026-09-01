class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        Scount = {}

        for char in s:
            Scount[char] = Scount.get(char, 0) + 1
        
        for char in t:
            if char not in Scount:
                return False
            
            Scount[char] -= 1

            if Scount[char] < 0:
                return False
        return True
            

