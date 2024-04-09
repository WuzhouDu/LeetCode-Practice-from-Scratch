class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        result = 0
        current = 0
        left = 0
        basket = {}
        for right in range(0, len(fruits)):
            if (fruits[right] in basket):
                basket[fruits[right]] += 1
                current += 1
                result = max(result, current)
            elif (len(basket) < 2):
                basket[fruits[right]] = 1
                current += 1
                result = max(result, current)
            else:
                while (left < right and len(basket) == 2):
                    basket[fruits[left]] -= 1
                    if (basket[fruits[left]] == 0):
                        basket.pop(fruits[left])
                    left += 1
                basket[fruits[right]] = 1
                current = right - left + 1
                result = max(result, current)
        return result