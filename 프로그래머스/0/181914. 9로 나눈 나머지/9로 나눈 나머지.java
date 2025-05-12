class Solution {
    public int solution(String number) {
        int answer = 0;
        String[] number_array = number.split("");
        for (String num: number_array) {
            answer += Integer.parseInt(num);
        }
        return answer % 9;
    }
}