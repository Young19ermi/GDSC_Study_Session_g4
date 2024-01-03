class Solution: 
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums2[j] < nums1[i]:
                j += 1

            else:
                return nums1[i]
        return -1

        #Time Limit Exceeded
        # i = 0
        # common = []
        # while i < len(nums1)-1:
        #     if nums1[i] in nums2:
        #         common.append(nums1[i]) 
        #     i+=1
        # return min(common)

        # Wrong Answer
        # i = 0
        # j = 0

        # while i < len(nums1)-1 and j < len(nums2)-1:
        #     if nums1[i] == nums2[j]:
        #         return nums1[i]
        #         break
        #     else:
        #         if len(nums1) > len(nums2):
        #             i+=1
        #         elif len(nums2) > len(nums1):
        #             j+=1
        #         else:
                    
        #             i+=1
        # return -1


        # Correct approach using set
        # countme = set(nums2)
        # ans = 0
        # for i in range(len(nums1)):
        #     if nums1[i] in countme:
        #         return nums1[i]
        #         break
        #     else:
        #         pass
        # return -1



        