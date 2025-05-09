import java.util.*;

class Solution {
    public int solution(int hp) {
        int answer = 0;
        for (int ant: new int[] {5, 3, 1}) {
            answer += hp / ant;
            hp %= ant;
        }
        return answer;
    }
}