package edu.ucsc;

import java.util.ArrayList;
import java.util.List;

/**
 * Leetcode Number: 118
 * Problem Name: Pascal's Triangle
 *
 * @author: Created by Xiaotong Li 
 * @time: 6/24/18:2018-06-24 23:08.
 */
public class generate {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> allRows = new ArrayList<List<Integer>>();
        ArrayList<Integer> row = new ArrayList<Integer>();
        for (int i = 0; i < numRows; i++) {
            row.add(0, 1);
            for (int j = 1; j < row.size() - 1; j++)
                row.set(j, row.get(j) + row.get(j + 1));
            allRows.add(new ArrayList<Integer>(row));
        }
        return allRows;
    }
}
