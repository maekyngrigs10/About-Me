import java.util.Scanner;

public class CalculatingEnergy {
    public static void main(String[] args) {
        Scanner ui = new Scanner(System.in);

        System.out.println("What is the weight of water? (numbers only)");
        double weight = ui.nextDouble();

        System.out.println("What is the intial temp of water? (numbers only)");
        double intial = ui.nextDouble();

        System.out.println("What is the final temp of water? (numbers only)");
        double last = ui.nextDouble();

        double energy = weight * (last-intial) * 4184;

        System.out.printf("energy needed: " + energy);

        ui.close();
    }
}
