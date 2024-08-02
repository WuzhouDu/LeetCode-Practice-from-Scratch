class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = {5: 0, 10: 0}
        for i in bills:
            if (i == 5):
                change[5] += 1
            elif (i == 10):
                change[10] += 1
                change[5] -= 1
                if (change[5] < 0):
                    return False
            else:
                if (change[10] > 0):
                    change[10] -= 1
                    change[5] -= 1
                    if (change[5] < 0):
                        return False
                else:
                    change[5] -= 3
                    if (change[5] < 0):
                        return False
        return True