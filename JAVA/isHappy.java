package edu.ucsc;

import java.util.HashSet;
import java.util.Set;

/**
 * Leetcode Number: 202
 * Problem Name: Happy Number
 *
 * @author: Created by Xiaotong Li 
 * @time: 6/29/18:2018-06-29 09:07.
 */
public class isHappy {
    public boolean isHappy(int n) {
        Set<Integer> inLoop = new HashSet<Integer>();
        int sum, remain;
        while (inLoop.add(n)){
            sum = 0;
            while (n > 0) {
                remain = n % 10;
                sum += remain * remain;
                n /= 10;
            }
            if (sum == 1){
                return true;
            }else {
                n = sum;
            }
        }
        return false;
    }
}
