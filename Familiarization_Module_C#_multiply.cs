using System;
using System.Collections.Generic;
using System.IO;

class Program {

    static int mul(int a, int b) { 
     return (a * b);
      
      
    }

    static void Main(String[] args) {
        int val1 = Convert.ToInt32(Console.ReadLine());
        int val2 = Convert.ToInt32(Console.ReadLine());
        int ret = mul(val1,val2);
        Console.WriteLine(ret);
    }
}      
