import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Deque<String> q = new ArrayDeque<>();

        int N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            String[] order = br.readLine().split(" ");
            switch (order[0]) {
                case "push":
                    q.add(order[1]);
                    break;
                case "pop":
                    String pop = q.isEmpty() ? "-1" : q.pop();
                    System.out.println(pop);
                    break;
                case "size":
                    System.out.println(q.size());
                    break;
                case "empty":
                    int isEmpty = q.isEmpty() ? 1 : 0;
                    System.out.println(isEmpty);
                    break;
                case "front":
                    String front = q.isEmpty() ? "-1" : q.peek();
                    System.out.println(front);
                    break;
                case "back":
                    String back = q.isEmpty() ? "-1" : q.peekLast();
                    System.out.println(back);
                    break;
            }
        }
        br.close();
    }
}
