import java.util.Scanner;

public class Calculator {
    int number1;
    int number2;

    public Calculator(int userChoice1,int userChoice2){
        number1 = userChoice1;
        number2 = userChoice2;
    }

    public void Addition(){
        System.out.println(number1+number2);
    }

    public void Subtraction(){
        System.out.println(number1-number2);
    }

    public void Multiplication(){
        System.out.println(number1*number2);
    }

    public void Division(){
        double newNumber = number1;
        double newNumber2 = number2;
        System.out.println(newNumber/newNumber2);
    }

    public void Remanding(){
        System.out.println(number1%number2);
    }

    public static void main(String[] args){
        Scanner input = new Scanner(System.in);

        System.out.print("Enter a number");
        int x = input.nextInt();

        System.out.print("Enter another number");
        int y = input.nextInt();

        Calculator operation1 = new Calculator(x,y);

        System.out.print("Enter a letter: ");
        String selected = input.next();

        switch (selected) {
            case "A" -> operation1.Addition();
            case "B" -> operation1.Subtraction();
            case "C" -> operation1.Multiplication();
            case "D" -> operation1.Division();
            case "E" -> operation1.Remanding();
            default -> System.out.println("Invalid Option");
        }
    }

}
