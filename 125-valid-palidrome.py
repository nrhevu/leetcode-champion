class Solution:
    def isPalindrome(self, s: str) -> bool:
        # lowercase and filter non-alphanumeric characters
        s = ''.join(c for c in s.lower() if c.isalnum())
        
        a = 0
        b = len(s) - 1
        while a < b:
            if s[a] != s[b]:
                return False
            a += 1
            b -= 1
        return True
        
print(Solution().isPalindrome("A man, a plan, a canal: Panama"))