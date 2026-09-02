class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        tracker = []

        for char in s:
            if char.isalnum():
                tracker += char.lower()
        
        if tracker == tracker[::-1]:
            return True
        return False