class FirstList(list):
    def __lt__(self, other):
        return self[0] < other[0]

class Solution:
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        h = list( FirstList(x) for x in intervals)
        heapq.heapify(h)
        print(h)
        
        ret = list()
        curr = heapq.heappop(h) if(h) else None

        while(h):
            x = heapq.heappop(h)
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
