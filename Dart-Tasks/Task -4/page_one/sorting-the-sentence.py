class Solution:
    def sortSentence(self, s: str) -> str:
        new_s = s.split()

        new_nums = []
        # for n in new:
        #     a = n[-1]
        #     print(a)
        #     res = sorted(new ,key =lambda x:  )
        #     print(res)
    
        for i in new_s:
            new_nums.append(i[-1])

        new_nums.sort()

        output = []
        for i in new_nums:
            for j in new_s:

                if i == j[-1]:
                    output.append(j[:-1])

        return " ".join(output)
