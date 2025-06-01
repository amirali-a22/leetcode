from typing import List

nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3


####
# nums1 = [0]
# m = 0
# nums2 = [1]
# n = 1
######
# nums1 = [1]
# m = 1
# nums2 = []
# n = 0


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1, p2, p = m - 1, n - 1, m + n - 1
        while p2 >= 0 and p1 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
        print(nums1)
        #
        # nums1 = nums1[:m]
        # nums1 += nums2
        # # print(nums1)
        # for i in range(len(nums1) - 1):
        #     if nums1[i] > nums1[i + 1]:
        #         temp = nums1[i]
        #         print(temp)
        #         nums1[i] = nums1[i + 1]
        #         nums1[i + 1] = temp
        # print(nums1)


s = Solution()
s.merge(nums1, m, nums2, n)
