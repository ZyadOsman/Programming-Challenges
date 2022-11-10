public class Calculator {


    private static int addition(int a, int b) {
        int answer = a + b;
        return answer;
    }
    private static int subtraction(int a, int b) {
        int answer = a - b;
        return answer;
    }
    private static int division(int a, int b) {
        int answer = a / b;
        return answer;
    }
    private static int multiplication(int a, int b) {
        int answer = a * b;
        return answer;
    }


    public static void main(String[] args) {
        String choice = args[0];

        switch (choice) {
            case "addition":
                int firstValue = Integer.parseInt(args[1]);
                int secondValue = Integer.parseInt(args[2]);
                int answer = addition(firstValue, secondValue);
                System.out.println(answer);
                break;
        }

        switch (choice) {
            case "subtraction":
                int firstValue = Integer.parseInt(args[1]);
                int secondValue = Integer.parseInt(args[2]);
                int answer = subtraction(firstValue, secondValue);
                System.out.println(answer);
                break;
        }
        switch (choice) {
            case "division":
                int firstValue = Integer.parseInt(args[1]);
                int secondValue = Integer.parseInt(args[2]);
                int answer = division(firstValue, secondValue);
                System.out.println(answer);
                break;
        }
        switch (choice) {
            case "multiplication":
                int firstValue = Integer.parseInt(args[1]);
                int secondValue = Integer.parseInt(args[2]);
                int answer = multiplication(firstValue, secondValue);
                System.out.println(answer);
                break;
        }




    }
}