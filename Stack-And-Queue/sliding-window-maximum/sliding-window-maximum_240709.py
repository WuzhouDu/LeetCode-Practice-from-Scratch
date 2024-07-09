from collections import deque 

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dequeue = deque()
        result = []
        # initialization
        for i in range(k):
            cur = nums[i]
            while (dequeue):
                if (dequeue[-1] < cur):
                    dequeue.pop()
                else:
                    break
            dequeue.append(cur)
        result.append(dequeue[0])
        
        for i in range(k, len(nums)):
            if (dequeue[0] == nums[i-k]):
                dequeue.popleft()

            cur = nums[i]
            while (dequeue):
                if (dequeue[-1] < cur):
                    dequeue.pop()
                else:
                    break
            dequeue.append(cur)
            result.append(dequeue[0])

        return result