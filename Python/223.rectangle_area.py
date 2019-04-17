class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        areaSum = (D - B) * (C - A) + (G - E) * (H - F)
#         max(min(C,G)-max(A,E), 0)*max(min(D,H)-max(B,F), 0)
        x1 = max(A, E)
        x2 = max(x1, min(C, G))
        y1 = max(B, F)
        y2 = max(y1, min(D, H))
        return areaSum - (x2 - x1) * (y2 - y1) 
