class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        count = Counter()
        
        ones_1 = []
        for i in range(len(img1)):
            for j in range(len(img1)):
                if img1[i][j] == 1:
                    ones_1.append((i,j))
        ones_2 = []
        for i in range(len(img1)):
            for j in range(len(img1)):
                if img2[i][j] == 1:
                    ones_2.append((i,j))
        
        for i, j in ones_1:
            for h, k in ones_2:
                count[(i - h, j - k)] += 1
        
        return max(count.values(), default=0)