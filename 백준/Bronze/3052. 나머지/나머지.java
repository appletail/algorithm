import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] remains = new int[42];
        for (int i = 0; i < 10; i++) {
            int number = Integer.parseInt(br.readLine());
            int remain = number % 42;
            remains[remain] = 1;
        }
        System.out.println(Arrays.stream(remains).sum());
        br.close();
    }
}
