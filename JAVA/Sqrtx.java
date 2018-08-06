package edu.ucsc;

public class Sqrtx {
   // Version 1: binary search
    public int mySqrt(int x) {
        if (x == 0) {
            return 0;
        }
        long start = 1;
        long end = x;
        while (start + 1 < end) {
            long mid = start + (end - start) / 2;
            if (mid * mid <= x) {
                start = mid;
            }else {
                end = mid;
            }
        }
        if (end * end < x) {
            return (int)end;
        }else {
            return (int)start;
        }
    }

    // Version 2 : Integer Newton
    public int mySqrt2(int x) {
        long r = x;
        while(r * r > x) {
            r = (r + x / r) / 2;
        }
        return (int)r;
    }
}



