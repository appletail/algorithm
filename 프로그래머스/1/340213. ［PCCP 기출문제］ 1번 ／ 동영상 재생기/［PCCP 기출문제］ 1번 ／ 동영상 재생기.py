def to_second(time):
    minute, second = map(int, time.split(':'))
    return minute * 60 + second

def to_minute(time):
    minute = time // 60
    second = time % 60
    if minute < 10:
        minute = f'0{minute}'
    if second < 10:
        second = f'0{second}'
        
    return f'{minute}:{second}'
    
def solution(video_len, pos, op_start, op_end, commands):
    video_len_second = to_second(video_len)
    pos_second = to_second(pos)
    op_start_second = to_second(op_start)
    op_end_second = to_second(op_end)
    
    if pos_second < 10:
        pos_second = 0
    elif pos_second > video_len_second-10:
        pos_second = video_len_second
    if op_start_second <= pos_second <= op_end_second:
        pos_second = op_end_second
        
    for command in commands:
        if command == 'next':
            pos_second += 10
        elif command == 'prev':
            pos_second -= 10
            
        if pos_second < 10:
            pos_second = 0
        elif pos_second > video_len_second-10:
            pos_second = video_len_second
        if op_start_second <= pos_second <= op_end_second:
            pos_second = op_end_second
            
    return to_minute(pos_second)
