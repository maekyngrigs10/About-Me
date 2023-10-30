import java.util.Scanner;
import java.lang.Math;

public class FinancialApp {
    public static void main(String[] args) {
        Scanner ui = new Scanner(System.in);

        System.out.println("What is investment amount? (numbers only)");
        double invest = ui.nextDouble();
        
        System.out.println("What is interest rate? (numbers only)");
        double interest = ui.nextDouble();

        System.out.println("What is the amount of years? (numbers only)");
        double years = ui.nextDouble();
        
        interest = interest*0.01;
        double months = years*12;
        double together = 1 + interest/12;
        double power = Math.pow(together,months);
        double future = invest*power;

        System.out.printf("future investment: $%2.2f%n",future);

        ui.close();
    }
}
