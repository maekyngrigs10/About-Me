public class book {
    //YOU DO NOT HAVE A main(String [] args) in this class!!!

    String title;
    String author;
    double rating;

    //no-args Constructors
    //def__init__(self):
    public book(){
    }
    
    //Constructor Signature
    public book(String title){
        //this.globalVar = localVar
        this.title = title;
    }

    public book(String title, String author){
        //this.globalVar = localVar
        this.title = title;
        this.author = author; 
    }

    public book(String title, String author, double rating){
        //this.globalVar = localVar
        this.title = title;
        this.author = author; 
        this.rating = rating;
    }

    @Override
    public String toString() {
        String out ="";
        out+="title: "+this.title;
        out+="\nauthor: "+this.author;
        out+="\nrating: "+this.rating+"/10";
        out+="\n";
        return out;
    }
}
