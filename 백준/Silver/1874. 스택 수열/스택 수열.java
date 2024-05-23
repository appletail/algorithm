import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder answer = new StringBuilder();

        int n = Integer.parseInt(br.readLine());
        int[] target = new int[n];
        for (int i=0; i<n; i++) target[i] = Integer.parseInt(br.readLine());

        Stack<Integer> stack = new Stack<>();
        int targetNum = 0;
        for (int i=1; i<=n; i++) {
            stack.push(i);
            answer.append("+\n");
            while (!stack.empty() && stack.peek() == target[targetNum]) {
                stack.pop();
                answer.append("-\n");
                targetNum++;
            }
        }
        if (stack.empty()) System.out.println(answer);
        else System.out.println("NO");
        br.close();
    }
}
