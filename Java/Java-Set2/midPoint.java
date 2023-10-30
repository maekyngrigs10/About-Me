import java.util.Scanner;
// import java.lang.Math;
public class midPoint{
    public static void main(String[]args){
        
      int x1 = 0;
      int y1 = 0;
      int x2 = 2;
      int y2 = 1;
      int x3 = 1;
      int y3 = 4;
      int x4 = 4;
      int y4 = 2;
      int x5 = 2;
      int y5 = 7;
      int x6 = 6;
      int y6 = 3;
      int x7 = 3;
      int y7 = 9;
      int x8 = 10;
      int y8 = 5;
      int x9 = 4;
      int y9 = 11;
      int x10 =12;
      int y10 =7;

      double midpoint1x = (x1+x2)/2 ; 
      double midpoint1y = (y1+y2)/2;
      double midpoint2x = (x3+x4)/2;
      double midpoint2y = (y3+y4)/2;
      double midpoint3x = (x5+x6)/2;
      double midpoint3y = (y5+y6)/2;
      double midpoint4x = (x7+x8)/2;
      double midpoint4y = (y7+y8)/2;
      double midpoint5x = (x9+x10)/2;  
      double midpoint5y = (y9+y10)/2;
        
    System.out.printf("\t a \t\t b \t\t\t Mid Point \n");
    System.out.println("\t("+x1+","+y1+")\t("+x2+","+y2+")"+"\t\t("+midpoint1x+","+midpoint1y+")");
    System.out.println("\t("+x3+","+y3+")\t("+x4+","+y4+")"+"\t\t("+midpoint2x+","+midpoint2y+")");
    System.out.println("\t("+x5+","+y5+")\t("+x6+","+y6+")"+"\t\t("+midpoint3x+","+midpoint3y+")");
    System.out.println("\t("+x7+","+y7+")\t("+x8+","+y8+")"+"\t\t("+midpoint4x+","+midpoint4y+")");
    System.out.println("\t("+x9+","+y9+")\t("+x10+","+y10+")"+"\t\t("+midpoint5x+","+midpoint5y+")");
 
    }
}