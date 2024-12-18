import java.util.*;

class Solution {
    public long solution(int n, int[] works) {
        long answer = 0;
        PriorityQueue<Long> maxHeapWorks = new PriorityQueue<>(Collections.reverseOrder());
        
        for (long work: works) {
            maxHeapWorks.offer(work);
        }
        
        
        while (n > 0) {
            if (maxHeapWorks.isEmpty()) {
                return 0;
            }
            
            long work = maxHeapWorks.poll();
            if (work > 1) maxHeapWorks.offer(work - 1);
            n -= 1;
        }
        
        for (long work: maxHeapWorks) {
            answer += Math.pow(work, 2);
        }
        
        return answer;
    }
}