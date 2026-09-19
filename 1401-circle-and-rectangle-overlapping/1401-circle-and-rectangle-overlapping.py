class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        if x2 < xCenter:
            clx = x2
        elif x1 > xCenter:
            clx = x1
        else:
            clx = xCenter
        
        if y2 < yCenter:
            cly = y2
        elif y1 > yCenter:
            cly = y1
        else:
            cly = yCenter

        return sqrt((xCenter - clx) ** 2 + (yCenter - cly) ** 2) <= radius