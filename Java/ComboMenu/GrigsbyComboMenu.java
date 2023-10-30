import java.util.Scanner;
import java.text.DecimalFormat;
// geeks for geeks bc everybody else just shows how to truncate the numbers

public class GrigsbyComboMenu{

    public static void main(String[] args) {
        DecimalFormat df = new DecimalFormat("0.00");
        Scanner ui = new Scanner(System.in);
        int orderNum = 1;
        double tax = 0.00;
        double finalTax = 0.00;
        double finalTotal = 0.00;
        double packetTotals = 0.00;
        double indTotal = 0.00;
        double totalFinal = 0.00;
        int sandwich = 0;
        int fries = 0;
        int drinks = 0;
        String finalOrder = "";
        String order = "-----------------------------\n\norder number:\t"+orderNum + "\nitem\t\t\tprice\n\n";

        System.out.println("if you are ready to order press 1 if not press 2");
        int choice = ui.nextInt();

        if (choice==1){
            while (true) {

            

                System.out.println("Menu:");
                System.out.println("1\tSandwiches: (tofu: $5.75, chicken: $5.25, beef: $6.25)");
                System.out.println("2\tFries: (small: $1, medium: $1.75, large: $2.25)(enter fries)");
                System.out.println("3\tDrinks: (small: $1, medium: $1.50, large: $2.00)(enter drink)");
                System.out.print("Enter your choice (1-3), 4 to add a new order, or 0 to finish ordering: ");
                choice = ui.nextInt();

                if(choice == 1){
                    System.out.println("1\ttofu: $5.75\n2\tchicken: $5.25\n3\tbeef: $6.25\n\n\n");

                    choice = ui.nextInt();

                    if(choice == 1){
                        indTotal += 5.75;
                        order += "tofu sandwich\t\t$5.75\n";
                        sandwich += 1;
                    } else if(choice==2){
                        indTotal += 5.25;
                        order += "chicken sandwich\t$5.25\n";
                        sandwich += 1;
                    }else if(choice==3){
                        indTotal += 6.25;
                        order += "beef sandwich\t\t$6.25\n";
                        sandwich += 1;
                    } else {
                        System.out.println("Invalid input, try again");
                    }
                    
                }else if(choice == 2){
                    System.out.println("1\tsmall: $1.25\n2\tmedium: $1.75\n3\tlarge: $2.25\n\n\n");

                    choice = ui.nextInt();

                    if(choice == 1){
                        indTotal += 1.25;
                        order += "small fries\t\t$1.25\n";
                        fries += 1;
                    } else if(choice==2){
                        indTotal += 1.75;
                        order += "medium fries\t\t$1.75\n";
                        fries += 1;
                    }else if(choice==3){
                        indTotal += 2.25;
                        order += "large fries\t\t$2.25\n";
                        fries += 1;
                    } else {
                        System.out.println("Invalid input, try again");
                    }
                }else if(choice == 3){
                    System.out.println("1\tsmall: $1.00\n2\tmedium: $1.50\n3\tlarge: $2.\n\n\n");
                    
                    choice = ui.nextInt();

                    if(choice == 1){
                        indTotal += 1.00;
                        order += "small drink\t\t$1.00\n";
                        drinks += 1;
                    } else if(choice==2){
                        indTotal += 1.50;
                        order += "medium drink\t\t$1.50\n";
                        drinks += 1;
                    }else if(choice==3){
                        indTotal += 2.00;
                        System.out.println("Would you like to upgrade to child-size for only 0.38¢ more? 1 for yes or 2 for no");
                        choice = ui.nextInt();
                        drinks += 1;
                        if(choice==1){
                            indTotal += 0.38;
                            order += "child size drink\t$2.38\n";
                        }else{
                            order += "large drink\t$2.00\n";
                        }
                    } else {
                        System.out.println("Invalid input, try again");
                    }

                }else if(choice == 4){
                    System.out.println("Would you like ketchup packets with that? (0.25¢ per) Whole,positive numbers only");

                    String choices = ui.next();

                    if(choices.contains("-")||choices.contains(".")){
                        System.out.println("That is not a valid input, try again");

                        System.out.println("Would you like ketchup packets with that? (0.25¢ per) Whole,positive numbers only");

                        choices = ui.next();

                        if(choices.contains("-")||choices.contains(".")){
                            System.out.println("That is not a valid, no ketchup for you");
                            order += "ketchups \t$"+df.format(packetTotals)+"\n";
                        } else if(choice<=0){
                            
                            choice = Integer.valueOf(choices);
                            indTotal += choice*0.25;
                            packetTotals = choice*0.25;
                            order += "ketchups(x"+choice+")\t\t$"+df.format(packetTotals)+"\n";
                        }
                    } else {
                        choice = Integer.valueOf(choices);
                        indTotal += choice*0.25;
                        packetTotals = choice*0.25;
                        order += "ketchups(x"+choice+")\t\t$"+df.format(packetTotals)+"\n";


                    }

                    if((sandwich> 0)&&(fries> 0)&&(drinks>0)){
                        indTotal -= 1;
                        order += "discount: \t\t$1.00";
                        sandwich = 0;
                        fries=0;
                        drinks = 0;
                    }

                    

                    tax = indTotal*0.07;
                    finalTotal += indTotal ;

                    finalTax+=tax;

                    

                    

                    order += String.format("\npre-tax:\t\t$"+df.format(indTotal));
                    order += String.format("\ntax:\t\t\t$"+df.format(tax));
                    order += String.format("\ntotal:\t\t\t$"+df.format(indTotal+tax));

                    System.out.println(order);

                    // System.out.printf("\npre-tax:\t\t$"+"%.2f",indTotal);
                    // System.out.printf("\ntax:\t\t\t$"+"%.2f",tax);
                    // System.out.printf("\ntotal:\t\t\t$"+"%.2f",finalTotal);
                    System.out.println("\n\n-----------------------------\n\n");

                    tax = 0.00;
                    orderNum += 1;

                    finalOrder += order;

                    order = "";

                    order += "\n\n-----------------------------\n\norder number:\t"+orderNum + "\nitem\t\t\tprice\n\n";

                    indTotal = 0;

                }else if(choice == 0){
                    System.out.println("Would you like ketchup packets with that? (0.25¢ per) Whole,positive numbers only");

                    String choices = ui.next();

                    if(choices.contains("-")||choices.contains(".")){
                        System.out.println("That is not a valid input, try again");

                        System.out.println("Would you like ketchup packets with that? (0.25¢ per) Whole,positive numbers only");

                        choices = ui.next();

                        if(choices.contains("-")||choices.contains(".")){
                            System.out.println("That is not a valid, no ketchup for you");
                            order += "ketchups \t$"+df.format(packetTotals)+"\n";
                        } else if(choice<=0){
                            
                            choice = Integer.valueOf(choices);
                            indTotal += choice*0.25;
                            packetTotals = choice*0.25;
                            order += "ketchups(x"+choice+")\t\t$"+df.format(packetTotals)+"\n";
                        }
                    } else {
                        choice = Integer.valueOf(choices);
                        indTotal += choice*0.25;
                        packetTotals = choice*0.25;
                        order += "ketchups(x"+choice+")\t\t$"+df.format(packetTotals)+"\n";


                    }

                    if((sandwich> 0)&&(fries> 0)&&(drinks>0)){
                        indTotal -= 1;
                        order += "discount: \t\t$1.00";
                        sandwich = 0;
                        fries=0;
                        drinks = 0;
                    }

                    tax = indTotal*0.07;
                    finalTax+=tax;

                    order += String.format("\npre-tax:\t\t$"+df.format(indTotal));
                    order += String.format("\ntax:\t\t\t$"+df.format(tax));
                    order += String.format("\ntotal:\t\t\t$"+df.format(indTotal+tax));

                    finalTotal += indTotal;

                    finalOrder += order;
                    // tax = finalTotal*0.07;
                    finalTax+=tax;
                    totalFinal = finalTotal + finalTax;


                    

                    System.out.println("Thanks for ordering at the Java Combo");
                    System.out.println(finalOrder);
                    System.out.println("\n\n-----------------------------\n\n");
                    System.out.printf("\npre-tax:\t\t$"+df.format(finalTotal));
                    System.out.printf("\ntax:\t\t\t$"+df.format(finalTax));
                    System.out.printf("\ntotal:\t\t\t$"+df.format(totalFinal));
                    
                    System.out.println("\n\n-----------------------------\n\n");

                    break;
                }else{
                    System.out.println("Invalid input, try again");
                }

                System.out.println(order);
                
            }

        }else{
            System.out.println("oh well then, goodbye");
        }
        ui.close();
    }
}