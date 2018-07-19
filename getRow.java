package edu.ucsc;

import java.util.ArrayList;
import java.util.List;

/**
 * Leetcode Number: 119
 * Problem Name: Pascal's Triangle II
 *
 * @author: Created by Xiaotong Li 
 * @time: 6/24/18:2018-06-24 23:33.
 */
public class getRow {
    public List<Integer> getRow(int rowIndex) {
        List<Integer> list = new ArrayList<Integer>();
        if (rowIndex < 0) {
            return list;
        }
        for (int i = 0; i < rowIndex + 1; i++) {
            list.add(0, 1);
            for (int j = 1; j < list.size() - 1; j++) {
                list.set(j, list.get(j) + list.get(j + 1));
            }
        }
        return list;

    }
}
