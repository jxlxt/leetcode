package edu.ucsc;

/* The guess API is defined in the parent class GuessGame.
   @param num, your guess
   @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
      int guess(int num); */

public class guessNumber extends GuessGame {
    public int guessNumber(int n) {
        if (n == 0) {
            return 0;
        }
        long start = 1;
        long end = n;
        while (start + 1 < end) {
            long mid = start + (end - start) / 2;
            if (guess[mid] == 0) {
                return mid;
            } else if (guess[mid] == -1) {
                start = mid;
            }else {
                end = mid;
            }
        }
        return (int)start;
    }
}