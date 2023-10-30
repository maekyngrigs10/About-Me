import java.util.Scanner;
import java.util.ArrayList;

public class inventoryExtra {
    public static void main(String[] args) {
        // program that keeps track of the animals at the Vet
        //  add, insert, remove, replace, clear the db
        // if the user types in quit -> the program ends

        ArrayList<String> petList = new ArrayList<String>();
        ArrayList<String> typeList = new ArrayList<String>();
        ArrayList<String> ageList = new ArrayList<String>();
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

                System.out.println("What type of animal is this furry friend?");

                userInput = ui.nextLine();

                typeList.add(userInput);

                System.out.println("How old is this furry friend? (include years and/or months)");

                userInput = ui.nextLine();

                ageList.add(userInput);

            }else if(userInput.equals("i")){
                System.out.println("insert");
                System.out.println("add");

                System.out.println("What furry friend would you like to insert?");
                userInput = ui.nextLine();

                System.out.println("Where would you like to insert this furry friend?");
                numInput = ui.nextInt();

                petList.add(numInput,userInput);

                System.out.println("How old is this furry friend you'd like to insert?");
                userInput = ui.nextLine();

                ageList.add(numInput,userInput);

                System.out.println("What type of animal is this furry friend you'd like to insert?");
                userInput = ui.nextLine();

                typeList.add(numInput,userInput);

            }else if(userInput.equals("d")){
                System.out.println("delete");

                System.out.println("What furry friend would you like to delete?");

                userInput = ui.nextLine();

                petList.indexOf(userInput);

                petList.remove(index);
                typeList.remove(index);
                ageList.remove(index);
                
            }else if(userInput.equals("r")){
                System.out.println("replace");

                System.out.println("What furry friend would you like to replace?");

                userInput = ui.nextLine();

                index = petList.indexOf(userInput);

                System.out.println("What furry friend would you like to replace it with?");

                userInput = ui.nextLine();

                petList.set(index,userInput);

                System.out.println("What is the age of this furry friend?");

                userInput = ui.nextLine();

                ageList.set(index,userInput);

                System.out.println("What type of animal is this furry friend?");

                userInput = ui.nextLine();

                typeList.set(index,userInput);
                
            }else if(userInput.equals("c")){
                System.out.println("clear");

                petList.clear();
                ageList.clear();
                typeList.clear();
                
            }else if(userInput.equals("v")){
                System.out.println("view");
                System.out.println("\tType\tName\tAge\t\n");
                for(int i=0;i<petList.size();i++){
                    
                    System.out.print("\t"+typeList.get(i)+"\t"+petList.get(i)+"\t"+ageList.get(i)+"\n");
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
