from collections import defaultdict


def solution(record):
    answer = []
    users = defaultdict(str)
    act_log_lst = {
        'Enter': '님이 들어왔습니다.',
        'Leave': '님이 나갔습니다.',
    }
    
    for r in record:
        splited_record = r.split(' ')
        if splited_record[0] != 'Leave':
            users[splited_record[1]] = splited_record[2]
        
        if splited_record[0] != 'Change':
            answer.append([splited_record[1], act_log_lst[splited_record[0]]])
    
    return [f'{users[uid]}{log}' for uid, log in answer ]
