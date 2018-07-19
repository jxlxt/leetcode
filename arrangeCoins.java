package edu.ucsc;

public class arrangeCoins {
    public int arrangeCoins (int n) {
        if (n == 0) {
            return 0;
        }
        long start = 1;
        long end = n;
        while (start + 1 < end) {
            long mid = start + (end - start) / 2;
            if (mid * (mid + 1) / 2 <= n) {
                start = mid;
            }else {
                end = mid;
            }
        }
        return (int)start;
    }
}
