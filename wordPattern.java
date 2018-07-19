package edu.ucsc;

import java.util.HashMap;

/**
 * Leetcode Number: 290
 * Problem Name: word pattern
 *
 * @author: Created by Xiaotong Li 
 * @time: 7/1/18:2018-07-01 10:29.
 */
public class wordPattern {
    public boolean wordPattern(String pattern, String str){            String[] arr= str.split(" ");
        HashMap<Character, String> map = new HashMap<Character, String>();
        if(arr.length!= pattern.length())
            return false;
        for(int i=0; i<arr.length; i++){
            char c = pattern.charAt(i);
            if(map.containsKey(c)){
                if(!map.get(c).equals(arr[i]))
                    return false;
            }else{
                if(map.containsValue(arr[i]))
                    return false;
                map.put(c, arr[i]);
            }
        }
        return true;
    }
}
