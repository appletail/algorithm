def solution(points, routes):
    answer = 0
    warehouse = [[0] * 101 for _ in range(101)]
    
    robots_loc = [[*points[route[0]-1]] for route in routes]
    is_robots_done = [0] * len(routes)
    cur_target = [1] * len(routes)
    
    visited = set()
    for r, c in robots_loc:
        warehouse[r][c] += 1
        if warehouse[r][c] >= 2:
            visited.add((r, c))     
    answer += len(visited)
    
    
    while sum(is_robots_done) < len(routes):
        for robot_num in range(len(routes)):
            cur_robot_loc = robots_loc[robot_num]
            if is_robots_done[robot_num]: 
                if sum(cur_robot_loc) != -2:
                    warehouse[cur_robot_loc[0]][cur_robot_loc[1]] -= 1
                    cur_robot_loc[0] = -1
                    cur_robot_loc[1] = -1
                continue

            cur_target_loc = points[routes[robot_num][cur_target[robot_num]]-1]
            warehouse[cur_robot_loc[0]][cur_robot_loc[1]] -= 1
            
            if cur_robot_loc[0] > cur_target_loc[0]:
                cur_robot_loc[0] -= 1
            elif cur_robot_loc[0] < cur_target_loc[0]:
                cur_robot_loc[0] += 1
            elif cur_robot_loc[1] > cur_target_loc[1]:
                cur_robot_loc[1] -= 1
            elif cur_robot_loc[1] < cur_target_loc[1]:
                cur_robot_loc[1] += 1

            warehouse[cur_robot_loc[0]][cur_robot_loc[1]] += 1
            if cur_robot_loc[0] == cur_target_loc[0] and cur_robot_loc[1] == cur_target_loc[1]:
                cur_target[robot_num] += 1
                if cur_target[robot_num] == len(routes[0]):
                    is_robots_done[robot_num] = 1
        
        visited = set()
        for r, c in robots_loc:
            if warehouse[r][c] >= 2:
                visited.add((r, c))        
            
        answer += len(visited)

    
    return answer