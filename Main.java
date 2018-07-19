package edu.ucsc;

import java.util.Scanner;
import java.lang.System;

public class Main {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        while(true) {
            String str = scan.next();
            int num = scan.nextInt();

            byte[] buf = str.getBytes();
            if(num < buf.length){
                int times = 0;
                for (int i = 0; i < num; i++){
                    if(buf[i] < 0){
                        times++;
                    }
                }
                if(times % 2 == 1){
                    num--;
                }
                System out = new String(buf, 0, num);
                System.out.println(out);
            }
        }
    }
}
