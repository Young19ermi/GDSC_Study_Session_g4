class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # counter = {num: nums.count(num) for num in nums}
        # d = {elem:value for elem,value in sorted(counter.items(), key = lambda x: x[1])}
        # new = {v: list(k for k in d if d[k] == v) for v in set(d.values())}
        # res= []
        # for key in new.keys():
        #     if len(new[key]) == 1:
        #         res.append(key * new[key])
        #     else:
        #         new[key].sort(reverse = True)
        #         res.append(key * new[key])

        # return itertools.chain.from_iterable(res)
        # Sorting based on count and values
        sorted_nums = sorted(nums, key=lambda x: (nums.count(x), -x), reverse=False)
        return sorted_nums


