import java.util.ArrayList;
import java.util.Scanner;

public class newLibrary {
    // private static ArrayList<Song> myPlaylist = new ArrayList<Song>();
    // private static ArrayList<book> myLibrary = new ArrayList<book>();
    // private static ArrayList<movie> myCinema = new ArrayList<movie>();

    public static void main(String[] args) {
        Scanner ui1 = new Scanner(System.in);


        ArrayList<Song> myPlaylist = new ArrayList<Song>();

        // myPlaylist.add(new Song("Hold Up","Pohl",10,5));
        // myPlaylist.add(new Song("Hmm Hmm Hmm", "TyMan",6,8));
        // myPlaylist.add(new Song("Blake Blucken", "Chick Filled A",1,1.5));
        // myPlaylist.add(new Song("Star Wars Last Jedi", "Georgy Porgy",1,3.6));
        // myPlaylist.add(new Song("Red", "Spinny Chair",9.9,3+47/60));


        // System.out.println(myPlaylist);

        // double durationOfPlaylist = 0.0;

        // for(int i=0;i<myPlaylist.size();i++){
        //     durationOfPlaylist += myPlaylist.get(i).getDuration();
        // }

        // System.out.println(durationOfPlaylist);


        // double avgDuration = durationOfPlaylist/myPlaylist.size();

        // System.out.println(avgDuration);

        String answer = "";


        while(true){
            System.out.println("would you like to (a)dd a song or (q)uit adding?");
            answer = ui1.nextLine().toString();

            if(answer.equals("a")){
                myPlaylist = addSong(myPlaylist);
            }else if(answer.equals("q")){
                break;
            }
            
            
        }
        for(int i=0;i<myPlaylist.size();i++){
                System.out.println(myPlaylist.get(i));
        }


        ui1.close();
    }

    public static ArrayList<Song> addSong(ArrayList<Song> arr){
        Scanner ui = new Scanner(System.in);
        System.out.println("Let's add to the playlist");
        System.out.println("What song would you like to add to the playlist?");
        String songName = ui.nextLine();

        System.out.println("What artist sings this song?");
        String artistName = ui.nextLine();

        System.out.println("What is the duration of this song ?");
        double duration = ui.nextDouble();

        System.out.println("What would you rate this song out of 10 this song?");
        double ranking = ui.nextDouble();

        Song songs = new Song(songName, artistName,ranking,duration);

        arr.add(songs);

        ui.close();



        return arr;


    }

    
}
