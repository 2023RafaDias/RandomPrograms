public class School {
    String name;
    int age;
    boolean enrolled;

    public School(String studentName,int studentAge, boolean studentEnrollment){
        name = studentName;
        age = studentAge;
        enrolled = studentEnrollment;
    }

    public void Grade(int minutesLate){
        System.out.println("Student "+ name+"!");
        System.out.println("You are "+minutesLate+" minutes late!");
    }
    public void increaseAge(int ageToAdd){
        int newAge = age + ageToAdd;
        age = newAge;
    }

    public static void main(String[] args) {
        School student1 = new School("Rafaela",15,true);
        School student2 = new School("Alexandre", 17,true);
        System.out.println(student1.age);
        System.out.println(student2.name);
        student1.Grade(10);
        student1.increaseAge(1);
        System.out.println(student1.age);
        int x = student1.age;
        switch (x){
            case 15:
                System.out.println("High Schooler");
                break;
            case 18:
                System.out.println("Graduated");
            default:
                System.out.println("Young");
        }
    }

}



