class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        interval = {}
        for i, (left, right, weight) in enumerate(intervals):
            if (left, right, weight) not in interval:
                interval[(left, right, weight)] = i

        intervals = sorted(interval)

        @cache
        def interDP(i, rem):
            if rem == 0 or i == len(intervals):
                return 0, []

            skip_weight, skip_indices = interDP(i+1, rem)

            left, right, weight = intervals[i]
            next_i = bisect.bisect_left(intervals, (right + 1,))
            next_weight, next_ind = interDP(next_i, rem - 1)
            take_weight = weight + next_weight
            take_ind = next_ind + [interval[intervals[i]]]
            take_ind.sort()

            if take_weight > skip_weight:
                return (take_weight, take_ind)
            elif take_weight < skip_weight:
                return (skip_weight, skip_indices)
            if take_ind < skip_indices:
                return (take_weight, take_ind)
            else:
                return (skip_weight, skip_indices)

        return interDP(0,4)[1]
