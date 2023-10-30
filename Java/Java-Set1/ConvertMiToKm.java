import java.util.Scanner;

public class ConvertMiToKm {
    public static void main(String[] args) {
        Scanner ui = new Scanner(System.in);

        System.out.println("Enter Miles");
        double miles = ui.nextDouble();

        System.out.printf(miles + " miles is equal to " + "%2.1f km %n",miles*1.6 );

        ui.close();
    }
}
