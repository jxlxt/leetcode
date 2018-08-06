package edu.ucsc;
/**
 * Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
 * The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.
 * You may assume that each input would have exactly one solution and you may not use the same element twice.
 * Input: numbers={2, 7, 11, 15}, target=9
 * Output: index1=1, index2=2
 **/

/**
 * leetcode number: 167
 * xiaotong li
 * 01/18/2018
 */

public class twoSumII {
    public static int[] twoSumII(int[] nums, int target){
        if(nums == null || nums.length < 2){
            return new int[]{-1, -1};
        }
        int left = 0;
        int right = nums.length - 1;
        while(left < right){
            int sum = nums[left] + nums[right];
            if (target == sum){
                return new int[]{left+1, right+1};
            }else if (target < sum){
                right--;
            }else {
                left++;
            }
        }
        return new int[]{-1, -1};
    }
}
