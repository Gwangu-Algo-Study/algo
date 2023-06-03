import java.util.Scanner;
public class Baek2231 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        Integer N_copy = N;
        int cnt = 0;
        while (N_copy > 1) {
            N_copy = N_copy/10;
            cnt += 1;
        }
       int result = 0;
        for (int i = (N - (9 * cnt)); i < N; i++) {
            int num = i;
            int sum = i;
            while (num != 0) {
                sum += num%10;
                num /= 10;
            }
            if (sum == N) {
                result = i;
                break;
            }
        }
        System.out.println(result);
    }
}
