months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
ps = [0] * 13
for m in range(1, 13): ps[m] = ps[m - 1] + months[m]

class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        aa = ps[int(arriveAlice[:2]) - 1] + int(arriveAlice[3:])
        la = ps[int(leaveAlice[:2]) -1] + int(leaveAlice[3:])
        ab = ps[int(arriveBob[:2]) - 1] + int(arriveBob[3:])
        lb = ps[int(leaveBob[:2]) -1] + int(leaveBob[3:])

        res = min(la, lb) - max(aa, ab) +1
        return max(res, 0)