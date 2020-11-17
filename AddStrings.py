class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        ret = []
        for (x,y) in zip_longest(reversed(num1), reversed(num2), fillvalue='0'):
            n = (ord(x) - ord('0')) +  (ord(y) - ord('0')) + carry
            (q, r) = divmod(n , 10)
            #print(x,y,q,r)
            ret.append(chr(ord('0') + r))
            carry = q
        if(carry):
            ret.append(chr(ord('0') + carry))
        #print(ret)
        return ''.join(reversed(ret))
