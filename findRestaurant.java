package edu.ucsc;

import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;

/**
 * Leetcode Number: 599
 * Problem Name: Minimum Index Sum of Two Lists
 *
 * @author: Created by Xiaotong Li 
 * @time: 7/3/18:2018-07-03 22:32.
 */
public class findRestaurant {
    public String[] findRestaurant(String[] list1, String[] list2){
        HashMap<String, Integer> map = new HashMap<String, Integer>();
        List<String> res = new LinkedList<String>();
        int minSum = Integer.MAX_VALUE;
        for (int i = 0; i < list1.length; i++) map.put(list1[i], i);
        for (int i = 0; i < list2.length; i++) {
            Integer j = map.get(list2[i]);
            if (j != null && i + j <= minSum) {
                if (i + j < minSum) {res.clear(); minSum = i + j;}
                res.add(list2[i]);
            }
        }
        return res.toArray(new String[res.size()]);
    }
}
