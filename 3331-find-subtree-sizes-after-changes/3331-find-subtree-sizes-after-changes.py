class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        adj = defaultdict(list)
        for i in range(1, n): adj[parent[i]].append(i)
        last = [-1] * 26

        def dfs(node):
            curr = ord(s[node]) - ord('a')
            prev = last[curr]
            if prev != -1: parent[node] = prev
            last[curr] = node
            for nei in adj[node]: dfs(nei)
            last[curr] = prev
        dfs(0)

        adj2 = defaultdict(list)
        for i in range(1, n): adj2[parent[i]].append(i)

        @cache
        def dfs2(node):
            total = 1
            for nei in adj2[node]: total += dfs2(nei)
            return total

        res =[]
        for i in range(n): res.append(dfs2(i))
        return res