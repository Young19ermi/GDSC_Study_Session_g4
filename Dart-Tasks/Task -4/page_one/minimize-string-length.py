class Solution:
    def minimizedStringLength(self, s: str) -> int:
        c = list(s)
        d =list(set(chr for chr in c))
        count = 0
        for chr in d:
            count +=1
        return count