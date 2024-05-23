import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String S = br.readLine();
        int[] count = new int[26];
        for (int i=0; i<count.length; i++) count[i] = -1;
        for (int i=0; i<S.length(); i++) {
            int str = S.charAt(i) - 97;
            if (count[str] == -1) count[str] = i;
        }
        for (int cnt: count) {
            System.out.print(cnt + " ");
        }
        br.close();
    }
}