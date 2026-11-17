class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)

        divisors = [[] for _ in range(n + 1)]
        for d in range(1, n):
            for m in range(2 * d, n + 1, d):
                divisors[m].append(d)

        cost = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1
                best = float("inf")
                for d in divisors[length]:
                    changes = 0
                    group_size = length // d
                    for r in range(d):
                        lo = i + r
                        hi = i + r + (group_size - 1) * d
                        while lo < hi:
                            if s[lo] != s[hi]:
                                changes += 1
                            lo += d
                            hi -= d
                    best = min(best, changes)
                cost[i][j] = best

        INF = float("inf")
        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for j in range(1, k + 1):
            for p in range(2 * j, n + 1):
                for q in range(2 * (j - 1), p - 1):
                    if dp[q][j - 1] != INF:
                        dp[p][j] = min(dp[p][j], dp[q][j - 1] + cost[q][p - 1])

        return dp[n][k]