import java.io.*;
import java.util.*;

public class Main {
    static boolean[][] graph;
    static int N, M, V;

    public static void dfs() {
        boolean[] visited = new boolean[N+1];
        LinkedList<Integer> stack = new LinkedList<>();
        stack.push(V);
        StringBuilder sb = new StringBuilder();

        while (!stack.isEmpty()) {
            int nodeFrom = stack.pop();
            if (!visited[nodeFrom]) sb.append(nodeFrom + " ");
            visited[nodeFrom] = true;

            for (int nodeTo = N; nodeTo > 0; nodeTo--) {
                if (graph[nodeFrom][nodeTo] && !visited[nodeTo]) {
                    stack.push(nodeTo);
                }
            }
        }
        System.out.println(sb);
    }

    public static void bfs() {
        boolean[] visited = new boolean[N+1];
        LinkedList<Integer> queue = new LinkedList<>();
        queue.add(V);
        visited[V] = true;

        StringBuilder sb = new StringBuilder();

        while (!queue.isEmpty()) {
            int nodeFrom = queue.pop();
            sb.append(nodeFrom + " ");

            for (int nodeTo = 1; nodeTo < N+1; nodeTo++) {
                if (graph[nodeFrom][nodeTo] && !visited[nodeTo]) {
                    visited[nodeTo] = true;
                    queue.add(nodeTo);
                }
            }
        }
        System.out.println(sb);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st1 = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st1.nextToken());
        M = Integer.parseInt(st1.nextToken());
        V = Integer.parseInt(st1.nextToken());

        graph = new boolean[N+1][N+1];
        while (M-- > 0) {
            StringTokenizer st2 = new StringTokenizer(br.readLine());
            int nodeA = Integer.parseInt(st2.nextToken());
            int nodeB = Integer.parseInt(st2.nextToken());
            graph[nodeA][nodeB] = true;
            graph[nodeB][nodeA] = true;
        }

        dfs();
        bfs();
        br.close();
    }
}
