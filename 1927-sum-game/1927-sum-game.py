class Solution:
    def sumGame(self, num: str) -> bool:
        sum1 , sum2 = 0, 0
        que1, que2 = 0, 0
        for i in range(len(num)):
            if i < len(num) // 2:
                if num[i] == "?":
                    que1 += 1
                else:
                    sum1 += int(num[i])
            else:
                if num[i] == "?":
                    que2 += 1
                else:
                    sum2 += int(num[i])
        
        return (que1 + que2) % 2 == 1 or  sum1 - sum2 != (que2 - que1) * 9 // 2