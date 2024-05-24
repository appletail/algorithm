import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int TC = Integer.parseInt(br.readLine());
        while (TC-- > 0) {
            String[] input = br.readLine().split(" ");
            int N = Integer.parseInt(input[0]);
            int M = Integer.parseInt(input[1]);

            LinkedList<int[]> q = new LinkedList<>();
            String[] nums = br.readLine().split(" ");
            for (int i=0; i<nums.length; i++) {
                q.add(new int[]{i, Integer.parseInt(nums[i])});  // 인덱스, 우선순위
            }

            int answer = 0;
            while (!q.isEmpty()) {
                int[] cur = q.pop();
                boolean isMax = true;
                for (int i=0; i<q.size(); i++) {
                    if (cur[1] < q.get(i)[1]) {
                        isMax = false;
                        q.add(cur);
                        break;
                    }
                }
                if (isMax) {
                    answer++;
                    if (cur[0] == M) {
                        System.out.println(answer);
                        break;
                    }
                }
            }
        }
    }
}
