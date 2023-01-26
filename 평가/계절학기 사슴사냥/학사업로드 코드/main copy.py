import random

DEER = 0
RABBIT = 1
SNAKE = 2

# ※ 전역변수 및 함수 사용 가능합니다
# ※ 단, 팀명을 앞에 prefix로 붙여주세요
#     ex) seoul12_2_sum = 0
#     ex) def seoul12_2() { } 
# ※ 현재 상태에서 빌드 시 사용할 수 있는 API는 사용 가능합니다
# ※ 제출방법 : Me 함수와 사용한 전역변수 또는 전역함수를 포함하여 txt 파일로 만들어서 제출


def 심(opp, turn, opp_prev, opp_last_pattern) :
    global gwangju1_9_snake_cnt3
    # 이 부분에 여러분의 알고리즘 구현이 들어갑니다
    if gwangju1_9_snake_cnt3 < 2:
        gwangju1_9_snake_cnt3 += 1
        return 2
    else:
        gwangju1_9_snake_cnt3 = 0
        return 0
    # 반드시 0 또는 1 또는 2로 리턴해야합니다

# 아래 Opponent1~3은 테스트용 상대 사냥꾼입니다
# 기본 제공 코드는 임의 수정해도 관계 없습니다
# 상대방 추가 시, Register 함수를 통해 상대방을 등록합니다. ex) Register("Opp1", "Opponent1")
def Opponent1(opp, turn, opp_prev, opp_last_pattern) :
    return SNAKE
    
def Opponent2(opp, turn, opp_prev, opp_last_pattern) :
    global gwangju1_9_rabbit_cnt
    # 이 부분에 여러분의 알고리즘 구현이 들어갑니다
    if gwangju1_9_rabbit_cnt < 2:
        gwangju1_9_rabbit_cnt += 1
        return RABBIT
    else:
        gwangju1_9_rabbit_cnt = 0
        return SNAKE
    
def Opponent3(opp, turn, opp_prev, opp_last_pattern) :
    global gwangju1_9_deer_cnt
    # 이 부분에 여러분의 알고리즘 구현이 들어갑니다
    if gwangju1_9_deer_cnt < 2:
        gwangju1_9_deer_cnt += 1
        return DEER
    else:
        gwangju1_9_deer_cnt = 0
        return SNAKE



def 노(opp, turn, opp_prev, opp_last_pattern) :
    # 이 부분에 여러분의 알고리즘 구현이 들어갑니다
    global gwangju1_9_snake_cnt2
    opp_deer_cnt = opp_last_pattern.count(0)
    opp_snake_cnt = opp_last_pattern.count(2)


    # 일단 사슴을 내서 내가 신뢰한다는 것을 보여준다
    if turn == 0:
        return 0

    # 첫 턴에서 상대방의 전략 확인
    if turn == 1:
        # 첫 매칭이거나 전판에서 첫 턴이 사슴이면 사슴
        if opp_prev == -1 or opp_prev == 0:
            return 0
        # 전판에서 첫 턴이 토끼면 뱀
        elif opp_prev == 1:
            gwangju1_9_snake_cnt2 += 1
            return 2
        # 전판에서 첫 턴이 뱀이면 뱀
        else:
            gwangju1_9_snake_cnt2 += 1
            return 2
    # 그 외 턴에서
    else:
        # 전역변수 내 뱀 카운트가 3이면 사슴내고 초기화
        if gwangju1_9_snake_cnt2 == 3:
            gwangju1_9_snake_cnt2 = 0
            return 0
        # 내가 첫매치거나 상대방 사슴 고른 수가 뱀 고른 수 보다 많으면 사슴
        if -1 in opp_last_pattern or (opp_deer_cnt > opp_snake_cnt):
            return 0
        # 아니면 뱀 카운트 늘리고 뱀
        else:
            gwangju1_9_snake_cnt2 += 1
            return 2


def 백(opp, turn, opp_prev, opp_last_pattern) :
    cnt=0
    deer=0
    rabbit=0
    snake=0
    for i in opp_last_pattern:
        for j in i:
            cnt+=1
            if j==-1:
                break
            elif j==0:
                deer+=1
            elif j==1:
                rabbit+=1
            elif j==2:
                snake+=1
    deer_percent=deer//cnt*100
    rabbit_percent=rabbit//cnt*100
    snake_percent=snake//cnt*100
    result=random.randrange(0,3)
    if snake_percent>80 or rabbit_percent>80:
        result=SNAKE
        return result
    if deer_percent>90:
        result=random.choice(0,2)
    # 이 부분에 여러분의 알고리즘 구현이 들어갑니다
    return result # 반드시 0 또는 1 또는 2로 리턴해야합니다

gwangju1_9_snake_cnt = 0
def 심백(opp, turn, opp_prev, opp_last_pattern) :
    global gwangju1_9_snake_cnt
    # 이 부분에 여러분의 알고리즘 구현이 들어갑니다
    if gwangju1_9_snake_cnt < 2:
        gwangju1_9_snake_cnt += 1
        result = SNAKE
    else:
        gwangju1_9_snake_cnt = 0
        result=DEER
    cnt=0
    deer=0
    rabbit=0
    snake=0
    for i in opp_last_pattern:
        for j in i:
            cnt+=1
            if j==-1:
                break
            elif j==0:
                deer+=1
            elif j==1:
                rabbit+=1
            elif j==2:
                snake+=1
    deer_percent=int((deer/cnt)*100)
    rabbit_percent=int((rabbit/cnt)*100)
    snake_percent=int((snake/cnt)*100)
    if snake_percent>80 or rabbit_percent>80:
        result=SNAKE
        return result
    if deer_percent>90:
        result=DEER
    # 이 부분에 여러분의 알고리즘 구현이 들어갑니다
    return result


def Register(name, func) :
    global f_inx
    names[f_inx] = name
    f[f_inx] = func
    f_inx += 1
    
########################## MAIN ##########################
노준호 = 0
백지원 = 0
심재원 = 0
심더하기백 = 0
뱀 = 0
토끼 = 0
사슴 = 0
for _ in range(1000):
    gwangju1_9_snake_cnt = 0
    gwangju1_9_snake_cnt2 = 0
    gwangju1_9_snake_cnt3 = 0
    gwangju1_9_deer_cnt = 0
    gwangju1_9_rabbit_cnt = 0

    f = [0] * 150
    names = [""] * 100
    f_inx = 0
    total_score = [0] * 150
    last_pattern = [[[0] * 10 for _ in range(150)] for _ in range(150)] 
    pattern_count = [0] * 150

    Register("심백", "심백")
    Register("노", "노")
    Register("백", "백")
    Register("심", "심")
    # Register("Opp1", "Opponent1")
    # Register("Opp2", "Opponent2")
    # Register("Opp3", "Opponent3")

    for i in range(140):
        for j in range(140):
            for k in range(10):
                last_pattern[i][j][k] = -1
                        
    for i in range(1, f_inx):
        for j in range(f_inx):
            team_a = j % f_inx
            team_b = (j+i) % f_inx
            
            # print(f"[{names[team_a]}] vs [{names[team_b]}]")
            
            a_game_score = 0
            b_game_score = 0
            
            prev_a = -1
            prev_b = -1
            
            team_a_count = 0
            team_b_count = 0
            
            a_pattern = [0] * 10
            b_pattern = [0] * 10
            
            for k in range(10):
                a = eval("{} (team_b, k, prev_b, last_pattern[team_b])".format(f[team_a]))
                b = eval("{} (team_a, k, prev_a, last_pattern[team_a])".format(f[team_b]))
                a_pattern[k] = a
                b_pattern[k] = b
                
                if a == prev_a: team_a_count += a+1
                else: team_a_count = 0
                if b == prev_b: team_b_count += b+1
                else: team_b_count = 0
                
                if a != 0 and a != 1 and a != 2: team_a_count = 100
                if b != 0 and b != 1 and b != 2: team_b_count = 100
                
                prev_a = a
                prev_b = b
                
                a_score = 0
                b_score = 0
                
                if a == DEER and b == DEER: a_score = 50; b_score = 50;
                elif a == DEER and b == RABBIT: a_score = 0; b_score = 20;
                elif a == DEER and b == SNAKE: a_score = 0; b_score = 10;
                elif a == RABBIT and b == DEER: a_score = 20; b_score = 0;
                elif a == RABBIT and b == RABBIT: a_score = 20; b_score = 20;
                elif a == RABBIT and b == SNAKE: a_score = 0; b_score = 30;
                elif a == SNAKE and b == DEER: a_score = 10; b_score = 0;
                elif a == SNAKE and b == RABBIT: a_score = 30; b_score = 0;
                elif a == SNAKE and b == SNAKE: a_score = 10; b_score = 10;
            
                a_score -= team_a_count
                b_score -= team_b_count
                
                a_bonus = random.randrange(3)
                b_bonus = random.randrange(3)
                a_score += a_bonus
                b_score += b_bonus
                
                a_game_score += a_score
                b_game_score += b_score
                
                a_str = "SNAKE" if a == 2 else "RABBIT" if a == 1 else "DEER"
                b_str = "SNAKE" if b == 2 else "RABBIT" if b == 1 else "DEER"
                
                # print(f"Turn [{k+1}] [{names[team_a]}:({a_str})] vs [{names[team_b]}:({b_str})] ---> score [{a_game_score}] / [{b_game_score}] ")
                
            for z in range(10):
                last_pattern[team_a][pattern_count[team_a]][z] = a_pattern[z]
                last_pattern[team_b][pattern_count[team_b]][z] = b_pattern[z]
                
            pattern_count[team_a] += 1
            pattern_count[team_b] += 1
                
            # print("<Game Result>")
            # if a_game_score == b_game_score: print("Draw")
            # else:
            #     pass
            #     print("Win : [{}]".format(names[team_a] if a_game_score > b_game_score else names[team_b]))
            # print()
            total_score[team_a] += a_game_score
            total_score[team_b] += b_game_score
                
    # print("<Final score>")
    max_inx = 0
    max_score = 0
    for i in range(f_inx):
        # print(f"[{names[i]}] Total Score : {total_score[i]}")
        if max_score < total_score[i]:
            max_inx = i
            max_score = total_score[i]
    if max_inx == 0:
        심더하기백 += 1
    elif max_inx == 1:
        노준호 += 1
    elif max_inx == 2:
        백지원 += 1
    elif max_inx == 3:
        심재원 += 1
    elif max_inx == 4:
        심더하기백 += 1
    elif max_inx == 5:
        심더하기백 += 1
    elif max_inx == 6:
        심더하기백 += 1
    # print(f"<Winner 최종 승자: [{names[max_inx]}] !!!>")
print(f'심재원:{심재원}; 노준호:{노준호}; 백지원:{백지원}; 심더하기백:{심더하기백} 뱀:{뱀}; 토끼:{토끼}; 사슴:{사슴}')

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        










