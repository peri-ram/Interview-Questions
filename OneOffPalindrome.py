class Solution:
    def isPalindrome(self, s, start, end):
        while(start < end):
            if(s[start] != s[end]):
                return (False, start, end)
            start += 1
            end   -= 1
        return (True, 0, 0)
    
    def validPalindrome(self, st: str) -> bool:
        (b, s,e) = self.isPalindrome(st, 0, len(st) -1)
        if(b): return True
        
        (b1, s1, e1) = self.isPalindrome(st, s+1, e)
        (b2, s2, e2) = self.isPalindrome(st, s, e-1)
        
        if(b1 or b2):
            return True
        else:
            print(f"Could not solve at indices {s} {e}")
            return False
