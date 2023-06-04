import java.util.Scanner;

public class Baek2609 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();

        System.out.println(little(N, M));
        System.out.println(big(N, M));
    }
    public static int little(int x,int y) {
        int result = 0;
        for (int i = Math.min(x,y); i > 0; i--) {
            if (x % i == 0 && y % i == 0) {
                result = i;
                break;
            }
        }
        return result;
    }
    public static int big(int x, int y) {
        int result = 0;
        for (int i = Math.max(x,y); i <= (x * y); i++) {
            if (i % x == 0 && i % y == 0) {
                result = i;
                break;
            }
        }
        return result;
    }
}
