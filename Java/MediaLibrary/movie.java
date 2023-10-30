public class movie {
    //YOU DO NOT HAVE A main(String [] args) in this class!!!

    String title;
    String director;
    double rating;

    //no-args Constructors
    //def__init__(self):
    public movie(){
    }
    
    //Constructor Signature
    public movie(String title){
        //this.globalVar = localVar
        this.title = title;
    }

    public movie(String title, String director){
        //this.globalVar = localVar
        this.title = title;
        this.director = director; 
    }

    public movie(String title, String director, double rank){
        
        this.title = title;
        this.director = director;
        this.rating = rank;
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

    public void setdirector(String newdirector){
        this.director = newdirector;
    }
    public String getdirector(){
        return this.director;
    }

    @Override
    public String toString() {
        String out ="";
        out+="title: "+this.title;
        out+="\ndirector: "+this.director;
        out+="\nrating: "+this.rating+"/10";
        out+="\n";
        return out;
    }
}
