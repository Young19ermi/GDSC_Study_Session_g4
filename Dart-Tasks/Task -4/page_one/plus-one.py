class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        integer = ""
        res= ""
        for num in digits:
            integer += str(num)
        

        i = str(int(integer) + 1)
        res = list(map(int, i))
        return res

        
        