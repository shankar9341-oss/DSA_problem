class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        avi = [[w,s] for s,w in enumerate(servers)]
        heapify(avi)
        using = []

        res = []
        for i in range(len(tasks)):
            while using and using[0][0] <= i:
                et, w, s = heappop(using)
                heappush(avi, [w, s])
            if avi:
                w, s = heappop(avi)
                heappush(using, [i + tasks[i], w, s])
            else:
                et, w, s = heappop(using)
                heappush(using, [et + tasks[i], w, s])
            res.append(s)
        return res