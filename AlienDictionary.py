#from typing import List, Set, Dict, Tuple, Optional

class Solution:
    def __init__(self):
        self.d = {}

    def initDict(self, order):
        for (i, a) in enumerate(order):
            self.d[a] = i
        print("Dict is", self.d)
        return

    def cmp_lessthan(self, w1, w2):
        for (c1, c2) in zip(w1, w2):
            o1 = self.d[c1]
            o2 = self.d[c2]
            if (o1 < o2):
                return True
            elif (o1 > o2):
                return False

        return (len(w1) <= len(w2))

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        self.initDict(order)

        if (len(words) < 2):
            return True

        for index in range(0, len(words) - 1):
            word1 = words[index]
            word2 = words[index + 1]
            if (not self.cmp_lessthan(word1, word2)):
                return False
        return True
