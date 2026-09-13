class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        cnt = Counter()
        
        ones1 = [(i, j) for i in range(len(img1)) for j in range(len(img1)) if img1[i][j]]
        ones2 = [(i, j) for i in range(len(img1)) for j in range(len(img1)) if img2[i][j]]
        
        for i, j in ones1:
            for h, k in ones2:
                cnt[(i - h, j - k)] += 1
        
        return max(cnt.values(), default=0)