class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # pos = set()
        # res = []
        # index = {num: index for index, num in enumerate(arr2)}
        # cansort = []
        # for n in arr2:
        #     pos.add(n)
        # for n in arr1:
        #     if n in pos:
        #         res.extend(sorted(arr1, key=lambda n: index.get(n, float('inf'))))
        #         break
        #     else:
        #         cansort.append(n)
        # return list(itertools.chain(res, sorted(cansort)))
  
        pos = set(arr2)
        res = []
        index = {num: index for index, num in enumerate(arr2)}
        cansort = []
        
        for n in arr1:
            if n in pos:
                res.append(n)
            else:
                cansort.append(n)
        
        res.sort(key=lambda n: index.get(n, float('inf')))
        cansort.sort()
        
        return res + cansort

       