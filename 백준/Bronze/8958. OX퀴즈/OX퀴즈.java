import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int TC = Integer.parseInt(br.readLine());
        for (int i = 0; i < TC; i++) {
            String quiz = br.readLine();
            int cnt = 0;
            int answer = 0;
            for (String OX: quiz.split("")) {
                if (OX.equals("O")) {
                    cnt += 1;
                    answer += cnt;
                } else cnt = 0;
            }
            System.out.println(answer);
        }
        br.close();
    }
}
