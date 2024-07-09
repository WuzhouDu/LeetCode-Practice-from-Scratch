import heapq

class Solution:
    def topKFrequent(self, nums, k):
        # 使用普通字典来统计每个数字出现的频率。
        frequencyMap = {}
        for num in nums:
            if num in frequencyMap:
                frequencyMap[num] += 1
            else:
                frequencyMap[num] = 1

        # 构建一个小顶堆，用于维护出现频率最高的k个数字。
        minHeap = []
        for num, freq in frequencyMap.items():
            # 如果堆还没满（即堆中元素少于k个），就直接添加当前元素
            if len(minHeap) < k:
                heapq.heappush(minHeap, (freq, num))
            # 如果堆已满，且当前元素的频率高于堆顶元素的频率，
            # 则替换堆顶元素（即频率最低的元素）。
            elif freq > minHeap[0][0]:
                heapq.heappushpop(minHeap, (freq, num))

        # 最后，从小顶堆中提取前k个频率最高的元素。
        topK = [num for freq, num in minHeap]
        return topK