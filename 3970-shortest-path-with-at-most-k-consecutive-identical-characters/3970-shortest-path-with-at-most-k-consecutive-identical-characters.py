class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        adj = defaultdict(list)
        for a, b, w in edges:
            adj[a].append((b, w))

        dist = [[inf] * (k + 1) for _ in range(n)]
        dist[0][1] = 0
        h = [(0, 0, 1)]

        while h:
            w, node, s = heapq.heappop(h)
            if w > dist[node][s]:
                 continue
            if node == n - 1: 
                return w

            for nei, nw in adj[node]:
                if labels[node] != labels[nei]: 
                    ns = 1
                else: 
                    ns = s + 1
                if ns > k: 
                    continue
                if dist[nei][ns] > w + nw:
                    dist[nei][ns] = w + nw
                    heapq.heappush(h, (w + nw, nei, ns))

        return -1