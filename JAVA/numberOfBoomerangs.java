package edu.ucsc;

import java.util.HashMap;
import java.util.Map;

/**
 * Leetcode Number: 447
 * Problem Name: Number of Boomerangs
 *
 * @author: Created by Xiaotong Li 
 * @time: 7/2/18:2018-07-02 20:20.
 */
public class numberOfBoomerangs {
    public int numberOfBoomerangs(int[][] points){
        int res = 0;
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        for (int i = 0; i < points.length; i++) {
            for (int j = 0; j < points.length; j++) {
                if (i == j) continue;
                int d = getDistance(points[i], points[j]);
                map.put(d, map.getOrDefault(d, 0) + 1);
            }

            for (int val: map.values()) {
                res += val * (val - 1);
            }
            map.clear();
        }
        return res;
    }

    private int getDistance(int[] a, int[] b) {
        int dx = a[0] - b[0];
        int dy = a[1] - b[1];

        return dx*dx + dy*dy;
    }
}
