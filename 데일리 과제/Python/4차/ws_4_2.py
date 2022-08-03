students = ['박해피', '이영희', '조민지', '조민지', 
            '김철수', '이영희', '이영희', '김해킹',
            '박해피', '김철수', '한케이', '강디티',
            '조민지', '박해피', '김철수', '이영희',
            '박해피', '김해킹', '박해피', '한케이','강디티']

students_votes = {}

for i in range(len(students)):
    if students[i] in students_votes:
        students_votes[students[i]] += 1
    else:
        students_votes[students[i]] = 1


b = sorted(students_votes.items(), key= lambda x : x[1], reverse = True)
b = dict(b)
print(b)