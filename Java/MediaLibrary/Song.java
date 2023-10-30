
public class Song {
    //YOU DO NOT HAVE A main(String [] args) in this class!!!

    String title;
    String artist;
    double rating;
    double duration;

    //no-args Constructors
    //def__init__(self):
    public Song(){
    }
    
    //Constructor Signature
    public Song(String title){
        //this.globalVar = localVar
        this.title = title;
    }

    public Song(String title, String artist){
        //this.globalVar = localVar
        this.title = title;
        this.artist = artist; 
    }

    public Song(String title, String artist, double rank){
        
        this.title = title;
        this.artist = artist;
        this.rating = rank;
    }

    public Song(String title, String artist, double rank,double time){
        
        this.title = title;
        this.artist = artist;
        this.rating = rank;
        this.duration = time;
    }

    //getters and setters
    //accessors and mutators

    //will have a getter and setter for each field variable (global variable)

    public void setRating(double newRating){
        this.rating = newRating;
    }
    public double getRating(){
        return this.rating;
    }

    public void setTitle(String newTitle){
        this.title = newTitle;
    }
    public String getTitle(){
        return this.title;
    }

    public void setArtist(String newArtist){
        this.artist = newArtist;
    }
    public String getArtist(){
        return this.artist;
    }

    public void setDuration(double newDuration){
        this.duration = newDuration;
    }

    public double getDuration(){
        return this.duration;
    }  


    @Override
    public String toString() {
        String out ="";
        out+="title: "+this.title;
        out+="\nartist: "+this.artist;
        out+="\nrating: "+this.rating+"/10";
        out+="\nduration: "+this.duration;
        out+="\n";
        return out;
    }
}
