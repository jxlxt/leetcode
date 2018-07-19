package edu.ucsc;

/**
 * Leetcode Number: 717
 * Problem Name: 1-bit and 2-bit Characters
 *
 * @Input: bits = [1, 0, 0]
 * @Output: True
 * Explanation: The only way to decode it is two-bit character and one-bit character.
 * So the last character is one-bit character.
 *
 * @Input: bits = [1, 1, 1, 0]
 * @Output: False
 * Explanation: The only way to decode it is two-bit character and two-bit character.
 * So the last character is NOT one-bit character.
 *
 * @author: Created by Xiaotong Li 
 * @time: 5/30/18:2018-05-30 23:38.
 */
public class isOneBitCharacter {
    public boolean isOneBitCharacter(int[] bits) {
        int i = 0; //the pointer from the first input
        int n = bits.length;
        while (i < n - 1){
            if (bits[i] == 0){
                i++;
            }else {
                i = i + 2;
            }
        }
        return i == n - 1;
    }
}
