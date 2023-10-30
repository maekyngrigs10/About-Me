import java.util.Scanner;


class XYZHospitalReports {
  public static void main(String[] args) {
    Scanner ui = new Scanner(System.in);

    System.out.println("What is your first name?");
    String firstName = ui.nextLine();
    
    System.out.println("What is your last name?");
    String lastName = ui.nextLine();

    System.out.println("What is your address?");
    String address = ui.nextLine();

    System.out.println("What is your city?");
    String city = ui.nextLine();

    System.out.println("What is your state?");
    String state = ui.nextLine();

    System.out.println("What is your zip code?");
    String zipCode = ui.nextLine();

    System.out.println("What is the amount owed?");
    String owedAmount = ui.nextLine();

    System.out.println("What is the amount you are paying?");
    String paidAmount = ui.nextLine();
    System.out.println("Payment date?");
    String paidDate = ui.nextLine();

    System.out.println("==========================================================================================");
    System.out.println("Name              Address               Payment Information");


    System.out.printf("last\tfirst\taddress\tcity\tstate\tzip\t amt owed\tamt paid\tpaid date\n");
      System.out.printf("%s\t%s\t%s\s%s,%s,\t%s\t\t$%s\t$%s\t%s%n",lastName,firstName,address,city,state,zipCode,owedAmount,paidAmount,paidDate );
    System.out.println("==========================================================================================");
    ui.close();
  }
}