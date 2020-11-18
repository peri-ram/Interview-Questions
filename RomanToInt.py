class Solution:

    def romanToInt(self, s: str) -> int:
        m = {
                'I' :            1,
                'V' :            5,
                'X' :            10,
                'L' :            50,
                'C' :            100,
                'D' :            500,
                'M' :            1000,
        }
    
        l = len(s)
        sum = 0
        for i in range(len(s)):
            curr_val = m[s[i]]
            next_val = m[s[i+1]] if (i+1 < l) else 0
            #print("Curr:%d Next:%d", curr_val, next_val)
            if (curr_val < next_val):
                sum -= curr_val
            else:
                sum += curr_val
                
        return sum
