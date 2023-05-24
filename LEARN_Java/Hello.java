public class FirstClass {
    public static void main(String[] args) {
        System.out.println("Hello World");

        boolean isAlien = false;
        if(isAlien == false){
            System.out.println("Not Alien");
        }

        int topScore = 10000;
        if (topScore == 100) {
            System.out.println("High score");
        }

        else if (topScore<100) {
            System.out.println("score < 100");
        }

        else if (topScore>100 && topScore == 1000) { //Logical AND operator
            System.out.println("Jackpot");
        }

        else if (topScore > 1000 || topScore == 10000) { //Logical OR operator
            System.out.println("Mega Jackpot");
        }

        else {
            System.out.println("Not high score");
        }

        int newValue = 50; //assigning value
        if (newValue == 50){ //equal value checking
            System.out.println("Error");
        }

        String carMake = "BMW";
        boolean isGood = carMake =="BMW" ? true: false; //Ternary operator

        System.out.println(isGood);

        double k1 = 20.00;
        double k2 = 81.00;
        double k3 = (k1+k2)*1.00;
        //System.out.println(k3);
        double k4 = k3%40.00;
        boolean k5 = k4 ==0.00? true:false;
        System.out.println(k5);
        if (k5==false){
            System.out.println("got some remainder");
        }
        /*String k6 = k5 == true? "none": "got some remainder";
        System.out.println(k6);*/

    }
}
