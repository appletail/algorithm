import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] target = new int[n];
        for (int i=0; i<n; i++) target[i] = Integer.parseInt(br.readLine());

        Stack<Integer> stack = new Stack<>();
        List<String> answer = new ArrayList<>();
        int targetNum = 0;
        for (int i=1; i<=n; i++) {
            stack.push(i);
            answer.add("+");
            while (!stack.empty() && stack.peek() == target[targetNum]) {
                stack.pop();
                answer.add("-");
                targetNum++;
            }
        }
        if (stack.empty()) for (String calc: answer) System.out.println(calc);
        else System.out.println("NO");
        br.close();
    }
}
