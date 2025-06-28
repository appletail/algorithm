class Solution {
    public int[] solution(int[] sequence, int k) {
        int start = 0;
        int end = 0;
        int curSum = 0;
        curSum += sequence[end];
        
        if (curSum == k) {
            return new int[] {0, 0};
        }
        
        int[] answer = {0, sequence.length};
        
        while (end < sequence.length && start < sequence.length) {
            if (curSum == k && end - start < answer[1] - answer[0]) {
                answer = new int[] {start, end};
            }
            
            if (curSum <= k && end < sequence.length-1) {
                end += 1;
                curSum += sequence[end];
            } else if (curSum > k && start < end) {
                curSum -= sequence[start];
                start += 1;
            } else {break;}
        }
        
        return answer;
    }
}