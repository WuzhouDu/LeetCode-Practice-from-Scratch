class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        result = 0
        targetMap1 = {}
        targetMap2 = {}
        for element1 in nums1:
            for element2 in nums2:
                if (element1 + element2) in targetMap1:
                    targetMap1[element1 + element2] += 1
                else: targetMap1[element1+ element2] = 1
        
        for element1 in nums3:
            for element2 in nums4:
                if (element1 + element2) in targetMap2:
                    targetMap2[element1 + element2] += 1
                else: targetMap2[element1+ element2] = 1

        for key1 in targetMap1.keys():
            if (-key1) in targetMap2:
                result += targetMap1[key1] * targetMap2[-key1]
            

        return result