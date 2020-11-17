class Solution:
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        h = list( (x[0], x) for x in intervals)
        heapq.heapify(h)
        print(h)
        
        ret = list()
        (_, curr) = heapq.heappop(h) if(h) else None

        while(h):
            (_, x) = heapq.heappop(h)
            #print("CURR", curr, "POP", x)
            if(x[0] <= curr[1]):
                curr[1] = max(curr[1], x[1])
            else:
                ret.append(curr)
                curr = x
            #print("RET", ret)
        if(curr):
            ret.append(curr)
        return ret
