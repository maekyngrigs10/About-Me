import java.util.Scanner;
import java.util.ArrayList;

public class inventory {
    public static void main(String[] args) {
        // program that keeps track of the animals at the Vet
        //  add, insert, remove, replace, clear the db
        // if the user types in quit -> the program ends

        ArrayList<String> petList = new ArrayList<String>();
        Scanner ui = new Scanner(System.in);


        String userInput = "";
        int numInput = 0;
        int index = 0;

        while(!userInput.equals("q")){

            System.out.println("What would you like to do? (a)dd, (i)nsert, (d)elete, (r)eplace, (c)lear, (v)iew or (q)uit");

            userInput = ui.nextLine();


            if(userInput.equals("a")){
                System.out.println("add");

                System.out.println("What furry friend would you like to add?");

                userInput = ui.nextLine();

                petList.add(userInput);

            }else if(userInput.equals("i")){
                System.out.println("insert");

                System.out.println("What furry friend would you like to insert?");

                userInput = ui.nextLine();

                System.out.println("Where would you like to insert this furry friend?");

                numInput = ui.nextInt();

                petList.add(numInput,userInput);

            }else if(userInput.equals("d")){
                System.out.println("delete");

                System.out.println("What furry friend would you like to delete?");

                userInput = ui.nextLine();

                petList.remove(userInput);
                
            }else if(userInput.equals("r")){
                System.out.println("replace");

                System.out.println("What furry friend would you like to replace?");

                userInput = ui.nextLine();

                index = petList.indexOf(userInput);

                System.out.println("What furry friend would you like to replace it with?");

                userInput = ui.nextLine();

                petList.set(index,userInput);
                
            }else if(userInput.equals("c")){
                System.out.println("clear");

                petList.clear();
                
            }else if(userInput.equals("v")){
                System.out.println("view");

                for(int i=0;i<petList.size();i++){
                    System.out.println(petList.get(i));
                }
            }else if(userInput.equals("q")){

            }else{
                System.out.println("Get ur crap together, try again");
            }
        }

        System.out.println("bye bye lil butterfly");

        ui.close();

    }
}
