import java.util.Scanner;

public class DrivingCost {
    public static void main(String[] args) {

        Scanner ui = new Scanner(System.in);

        System.out.println("How far of distance?");
        double distance = ui.nextDouble();

        System.out.println("How many miles per gallon?");
        double mpg = ui.nextDouble();

        System.out.println("Cost of gas per gallon?");
        double cost = ui.nextDouble();

        double total = (distance/mpg) * cost;

        System.out.printf("$%2.2f%n",total);
        ui.close();
        
    }
}
