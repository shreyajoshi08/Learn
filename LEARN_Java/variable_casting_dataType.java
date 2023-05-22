

// Online Java Compiler
// Use this editor to write, compile and run your Java code online

public class Hello {
    public static void main(String[] args) {
        //System.out.println("Hello World");
        
        int myFirstNum = 5;
        //System.out.println(myFirstNum);
        
        int mySecondNum = 12;
        //System.out.println(mySecondNum);
        
        int myThirdNum = 6;
        //System.out.println(myThirdNum);
        
        int myTotal = myFirstNum+mySecondNum+myThirdNum;
        //System.out.println(myTotal);
        
        float k = 3f/2f;
        //System.out.println(k);
        int m = (int)(k);
        //System.out.println(m);
        
        byte a = 10;
        short b = 20;
        int c = 50;
        long d = 50000+10*(a+b+c);
        //System.out.println(d);
        
        double no_of_kilo = 10;
        double no_of_pounds = 200d;
        double no_of_pounds_to_kilo = 0.45359237d * no_of_pounds;
        double no_of_kilo_to_pounds = no_of_kilo/0.45359237d;
        System.out.println(no_of_pounds_to_kilo);
        
        System.out.println(no_of_kilo_to_pounds);
        
    }
} 


/*
ADDITIONAL CASTING EXAMPLES
public class Main {
  public static void main(String[] args) {
    int myInt = 9;
    double myDouble = myInt; // Automatic casting: int to double

    System.out.println(myInt);      // Outputs 9
    System.out.println(myDouble);   // Outputs 9.0
  }
}


public class Main {
  public static void main(String[] args) {
    double myDouble = 9.78d;
    int myInt = (int) myDouble; // Manual casting: double to int

    System.out.println(myDouble);   // Outputs 9.78
    System.out.println(myInt);      // Outputs 9
  }
}


*/
