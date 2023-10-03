from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 1
    bridge = deque([(truck_weights[0], bridge_length + 1)])
    cur_truck_weight = truck_weights[0]
    cur_truck_count = 1
    truck_idx = 1
    
    while bridge:
        answer += 1
        if bridge[0][1] == answer:
            cur_truck_count -= 1
            cur_truck_weight -= bridge[0][0]
            bridge.popleft()

        if truck_idx < len(truck_weights):
            if cur_truck_count + 1 <= bridge_length and cur_truck_weight + truck_weights[truck_idx] <= weight:
                bridge.append((truck_weights[truck_idx], answer + bridge_length))
                cur_truck_count += 1
                cur_truck_weight += truck_weights[truck_idx]
                truck_idx += 1

    return answer