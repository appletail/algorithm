def solution(skill, skill_trees):
    answer = 0
    skill_index = {skill[i]: i for i in range(len(skill))}
    for skill_tree in skill_trees:
        is_run = [False] * len(skill)
        for s in skill_tree:
            if (idx := skill_index.get(s)) != None:
                if idx == 0:
                    is_run[idx] = True
                else:
                    if not is_run[idx-1]:
                        break
                    is_run[idx] = True
        else:
            answer += 1
            
    return answer