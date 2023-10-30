import java.util.Scanner;
import java.lang.Math;

class Main {
  public static void main(String[] args) {
    Scanner ui = new Scanner(System.in);

    System.out.println("What is the length of the side");
    double side = ui.nextDouble();
    double root = (Math.sqrt(3))/4;


    double area = (root*(side*side));
    double volume = (area * side);

    System.out.println("area: " + String.format("%.2f",area) + "\n volume:" +String.format("%.2f",volume));
    
    
    ui.close();
    
  }
}