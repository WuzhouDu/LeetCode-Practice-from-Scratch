class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        shorter = nums1 if len(nums1) < len(nums2) else nums2
        longer = nums2 if len(nums1) < len(nums2) else nums1
        mapShort = {}
        result = []
        for element in shorter:
            if (element in mapShort):
                continue
            else:
                mapShort[element] = 1
        for element in longer:
            if (element in mapShort):
                del mapShort[element]
                result.append(element)

        return result
