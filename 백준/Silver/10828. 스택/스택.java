import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        LinkedList<String> s = new LinkedList<>();

        int N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            String[] order = br.readLine().split(" ");
            switch (order[0]) {
                case "push":
                    s.push(order[1]);
                    break;
                case "pop":
                    String pop = s.isEmpty() ? "-1" : s.pop();
                    System.out.println(pop);
                    break;
                case "size":
                    System.out.println(s.size());
                    break;
                case "empty":
                    int isEmpty = s.isEmpty() ? 1 : 0;
                    System.out.println(isEmpty);
                    break;
                case "top":
                    String top = s.isEmpty() ? "-1" : s.peek();
                    System.out.println(top);
                    break;
            }
        }
        br.close();
    }
}
