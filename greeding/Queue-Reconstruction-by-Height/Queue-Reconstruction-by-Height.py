class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort()
        result = [[-1, -1] for _ in range(len(people))]
        for height, amt in people:
            target = amt
            available = 0
            for i in range(len(result)):
                if (available == target and result[i][0] == -1):
                    result[i] = [height, amt]
                    break
                if (result[i][0] == height):
                    target -= 1
                if (result[i][0] == -1):
                    available += 1
                
        return result