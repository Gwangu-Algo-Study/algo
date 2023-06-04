import java.util.Scanner;

public class Baek11050 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int K = sc.nextInt();
        int x = 1;
        int y = 1;
        for (int i = N; i > K; i--) {
            x *= i;
            y *= (i-K);
        }

        int result = x/y;
        System.out.println(result);
    }
}
