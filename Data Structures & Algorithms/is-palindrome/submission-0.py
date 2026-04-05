class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(' ', '')
        s = ''.join(char for char in s if char.isalnum())


        if len(s) % 2 != 0:
            return s[:(len(s)//2)].lower() == ''.join(reversed(list(s[1+len(s)//2:]))).lower()
        
        else:
            return s[:(len(s)//2)].lower() == ''.join(reversed(list(s[len(s)//2:]))).lower()