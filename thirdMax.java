package edu.ucsc;

/**
 * Leetcode Number: 414
 * Problem Name: Third Maximum Number
 *
 * @author: Created by Xiaotong Li 
 * @time: 6/26/18:2018-06-26 08:57.
 */
public class thirdMax {
    public int thirdMax(int[] nums) {
        Integer max1 = null;
        Integer max2 = null;
        Integer max3 = null;
        for (Integer i : nums) {
            if (i.equals(max1) || i.equals(max2) || i.equals(max3)) continue;
            if (max1 == null || i > max1){
                max3 = max2;
                max2 = max1;
                max1 = i;
            }else if (max2 == null || i > max2) {
                max3 = max2;
                max2 = i;
            }else if (max3 == null || i > max3) {
                max3 = i;
            }
        }
        return max3 == null ? max1 : max3;
    }
}
