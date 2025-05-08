import java.util.*;

class Solution {
    public String[] solution(String my_string) {
        List<String> answer = new ArrayList<>();
        String cur = "";
        for (int i = 0; i < my_string.length(); i++) {
            char str = my_string.charAt(i);
            if (str == ' ') {
                if (!cur.equals("")) {
                    answer.add(cur);
                }
                cur = "";
            } else {
                cur += str;
            }
        }
        
        if (!cur.equals("")) {
            answer.add(cur);
        }
        
        return answer.toArray(new String[0]);
    }
}