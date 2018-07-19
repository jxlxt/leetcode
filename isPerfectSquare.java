package edu.ucsc;

/**
 * @param num an positive integer number
 * @return boolean value if num is a perfect square true else false
 */
public class isPerfectSquare {
    public boolean isPerfectSquare (int num) {
                if ( num == 0) {
                    return false;
                }
                long start = 1;
                long end = num;
                while (start + 1 < end) {
                    long mid = start + (end - start ) / 2;
                    if (mid * mid <= num) {
                        start = mid;
                    }else {
                        end = mid;
                    }
                }
                return start * start == (long)num || end * end == (long)num;

    }
}
