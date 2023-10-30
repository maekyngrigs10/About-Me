import java.util.Scanner;
import java.lang.Math;
public class triangleArea {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the coordinates of three points (x1, y1), (x2, y2), and (x3, y3):");
        double x1 = scanner.nextDouble();
        double y1 = scanner.nextDouble();
        double x2 = scanner.nextDouble();
        double y2 = scanner.nextDouble();
        double x3 = scanner.nextDouble();
        double y3 = scanner.nextDouble();
        double area = calculateTriangleArea(x1, y1, x2, y2, x3, y3);
        System.out.println("The area of the triangle is: " + area);
        scanner.close();
    }
    public static double calculateTriangleArea(double x1, double y1, double x2, double y2, double x3, double y3) {
        return 0.5*Math.abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2));
    }
}