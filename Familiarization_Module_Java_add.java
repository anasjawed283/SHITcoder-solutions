import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Main {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int a = input.nextInt();
        int b = input.nextInt();
        int ret = add(a,b);        
        System.out.println(ret);
    }
    
    public static int add(int x, int y) {
        return x + y;
    }
}