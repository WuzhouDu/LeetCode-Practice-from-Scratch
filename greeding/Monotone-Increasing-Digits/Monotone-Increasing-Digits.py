class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        integerArr = list(str(n))
        # for i in range(len(integerArr)):
        #     integerArr[i] = int(integerArr[i])
        def recurse(start):
            if (start == len(integerArr)-1):
                return
            if (integerArr[start+1] >= integerArr[start]):
                recurse(start+1)
                if (integerArr[start+1] >= integerArr[start]):
                    return
            integerArr[start] = str(int(integerArr[start]) - 1)
            for i in range(start+1, len(integerArr)):
                integerArr[i] = '9'
            return
        recurse(0)
        return int("".join(integerArr))