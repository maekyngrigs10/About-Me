import java.util.Scanner;


class minuteToYear {
  public static void main(String[] args) {
        Scanner ui = new Scanner(System.in);
        
        System.out.println("Enter minutes: ");

        int minutes = ui.nextInt();
        int display = minutes;

        int years = 0;
        int days = 0;

        while (minutes >= 525600){
            minutes -= 525600;
            years += 1;
        }

        while (minutes >= 1440){
            minutes -= 1440;
            days += 1;
    }

      System.out.printf(" %s minutes is equal to %s years and %s days",display,years,days);

        ui.close();
  }
}