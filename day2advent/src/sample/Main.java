package sample;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) throws FileNotFoundException {
        File file = new File("C:\\Users\\Fergu\\Documents\\AdventOfCode2020\\inputday2.txt");
        Scanner sc = new Scanner(file);

        int min,max, mainCount, countPassword;
        char letter;
        char[] array;
        String password;
        mainCount = 0;
        while (sc.hasNextLine()) {
            String wholeThing = sc.nextLine();
            min = Integer.parseInt(wholeThing.substring(0,wholeThing.indexOf("-")));
            max = Integer.parseInt(wholeThing.substring(wholeThing.indexOf("-")+1,wholeThing.indexOf(" ")));
            letter = wholeThing.substring(wholeThing.indexOf(" ")+1, wholeThing.indexOf(":")).charAt(0);
            // Part 1 array = wholeThing.substring(wholeThing.indexOf(":")+1, wholeThing.length()).toCharArray();
            password = wholeThing.substring(wholeThing.indexOf(":")+1, wholeThing.length());

            // Part 2
            if (password.charAt(min) == letter || password.charAt(max) == letter) {
                if (password.charAt(min) == letter && password.charAt(max) == letter) {
                    // Do nothing
                } else {
                    mainCount++;
                }
            }

            /* Part 1
            countPassword = 0;
            for (char myCharacter : array) {
                if (myCharacter == letter) {
                    countPassword++;
                }
            }

            if (countPassword >= min && countPassword <= max) {
                mainCount++;
            }

             */
        }
        System.out.println(mainCount);
    }
}
