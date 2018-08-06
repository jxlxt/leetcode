package edu.ucsc;

/**
 * Leetcode Number: 852
 * Problem Name: Peak Index in a Mountain Array
 *
 * @author: Created by Xiaotong Li 
 * @time: 7/4/18:2018-07-04 10:19.
 */
//binary search
//public int peakIndexInMountainArray(int[] A) {
//        int lo = 0, hi = A.length - 1;
//        while (lo < hi) {
//          int mi = lo + (hi - lo) / 2;
//          if (A[mi] < A[mi + 1])
//              lo = mi + 1;
//          else
//              hi = mi;
//              }
//        return lo;
//       }
/**
 * a good solution for this problem is binary search
 * but if there is a follow-up question for better solution
 * we can use golden search algorithm
 */
public class peakIndexInMountainArray {
    private int gold1(int left, int right) {
        int result = (int)(Math.round((right - left) * 0.382));
        return left + result;
    }
    private int gold2(int left, int right) {
        int result = (int)(Math.round((right - left) * 0.618));
        return left + result;
    }
    public int peakIndexInMountainArray(int[] A) {
        int left = 0, right = A.length - 1;
        int x1 = gold1(left, right);
        int x2 = gold2(left, right);
        while (x1 < x2) {
            if (A[x1] < A[x2]) {
                left = x1;
                x1 = x2;
                x2 = gold1(x1, right);
            }else {
                right = x2;
                x2 = x1;
                x1 = gold2(left, x2);
            }
        }
        return x1;
    }
}
