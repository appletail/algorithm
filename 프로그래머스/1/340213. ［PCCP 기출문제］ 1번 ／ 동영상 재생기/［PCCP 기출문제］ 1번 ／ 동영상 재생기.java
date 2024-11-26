class Solution {
    public int to_second(String time) {
        String[] splited_time = time.split(":");
        return Integer.parseInt(splited_time[0]) * 60 + Integer.parseInt(splited_time[1]);
    }
    
    public String to_minute(int time) {
        int minute = time / 60;
        int second = time % 60;
        return String.format("%02d:%02d", minute, second);
    }
    
    public String solution(String video_len, String pos, String op_start, String op_end, String[] commands) {
        int video_len_second = to_second(video_len);
        int pos_second = to_second(pos);
        int op_start_second = to_second(op_start);
        int op_end_second = to_second(op_end);
        
        if (pos_second < 10) {pos_second = 0;}
        else if (pos_second > video_len_second-10) {pos_second = video_len_second;}
        if (op_start_second <= pos_second && pos_second <= op_end_second) {pos_second = op_end_second;}
        
        
        for (String command: commands) {            
            if (command.equals("next")) {pos_second += 10;}
            else if (command.equals("prev")) {pos_second -= 10;}

            if (pos_second < 10) {pos_second = 0;}
            else if (pos_second > video_len_second-10) {pos_second = video_len_second;}
            if (op_start_second <= pos_second && pos_second <= op_end_second) {pos_second = op_end_second;}
        }
        
        return to_minute(pos_second);
    }
}