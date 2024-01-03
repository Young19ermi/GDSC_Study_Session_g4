class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        # i = 0
        # j = 0
        # while i < len(nums1)-1 and j < len(nums2)-1:
        #     if nums1[i] not in nums2:
        #         i += 1
        #     else:
        #         return i+1
        # return -1

        countme = set(nums2)
        ans = 0
        for i in range(len(nums1)):
            if nums1[i] in countme:
                return nums1[i]
                break
            else:
                pass
        return -1



        