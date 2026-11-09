class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        available = SortedList([i for i in range(k)])
        using = SortedList()
        res = [0] * k
        n = len(arrival)

        for i in range(n):
            while using and using[0][0] <= arrival[i]:
                s = using.pop(0)[1] % k
                available.add(s)
            if available:
                idx = available.bisect_left(i % k)
                if idx == len(available):
                    idx = 0
                s = available.pop(idx)
                using.add((arrival[i]+load[i], s))
                res[s] += 1

        mx = max(res)
        out = []
        for i in range(k):
            if res[i] == mx: out.append(i)
        
        return out
