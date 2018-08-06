package edu.ucsc;

/**
 * Leetcode Number: 121
 * Problem Name: Best Time to Buy and Sell Stock
 *
 * @author: Created by Xiaotong Li 
 * @time: 6/24/18:2018-06-24 23:49.
 */
public class maxProfit {
    public int maxProfit(int[] prices) {
        if (prices == null || prices.length < 2) {
            return 0;
        }
        int maxCur = 0, maxPro = 0;
        for (int i = 1; i < prices.length; i++) {
            maxCur = Math.max(0, maxCur += prices[i] - prices[i - 1]);
            maxPro = Math.max(maxCur, maxPro);
        }
        return maxPro;
    }
}
