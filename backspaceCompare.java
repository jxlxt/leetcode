package edu.ucsc;

/**
 * Leetcode Number: 844
 * Problem Name: Backspace String Compare
 *
 * @author: Created by Xiaotong Li 
 * @time: 7/4/18:2018-07-04 09:54.
 */
public class backspaceCompare {
    private String getString(String str){
        int n = str.length(), count = 0;
        String result = "";
        for(int i=n-1; i>=0; i--) {
            char ch=str.charAt(i);
            if(ch=='#')
                count++;
            else {
                if(count>0)
                    count--;
                else {
                    result += ch;
                }
            }
        }
        return result;
    }
    public boolean backspaceCompare(String S, String T) {
        return getString(S).equals(getString(T));
    }
}
