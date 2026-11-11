class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        if cost1 + cost2 <= costBoth:
            return cost1 * need1 + cost2 * need2
        if need1 <= need2:
            res = costBoth *need1
            need2 -= need1
            return res + need2 * min(cost2, costBoth)
        else:
            res = costBoth * need2
            need1 -= need2
            return res + need1 * min(cost1, costBoth)