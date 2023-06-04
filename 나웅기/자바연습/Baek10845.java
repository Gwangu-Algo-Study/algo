
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Scanner;

public class Baek10845 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        Deque<Integer> arr = new ArrayDeque();
        for (int i = 0; i < N; i++) {
            String[] input = br.readLine().split(" ");
            String word = input[0];
            switch(word) {
                case "push" :
                    int x = Integer.parseInt(input[1]);
                    arr.addLast(x);
                break;
                case "pop" : if (arr.size() > 0) {
                    System.out.println(arr.getFirst());
                    arr.pollFirst();
                } else {
                    System.out.println(-1);
                }
                break;
                case "size" : System.out.println(arr.size());
                break;
                case "empty" : if (arr.size() == 0) {
                    System.out.println(1);
                } else {
                    System.out.println(0);
                }
                break;
                case "front" : if (arr.size() == 0) {
                    System.out.println(-1);
                    break;
                } else {
                    System.out.println(arr.getFirst());
                }
                break;
                case "back" : if (arr.size() == 0) {
                    System.out.println(-1);
                    break;
                } else {
                    System.out.println(arr.getLast());
                }
                    break;
            }
        }
    }
}
