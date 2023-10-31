import sys
input = sys.stdin.readline

num_stuffs, max_weight = map(int, input().split())
stuffs = []

for i in range(num_stuffs):
    weight, value = map(int, input().split())
    stuffs.append((weight, value))

def find_max(cursor, current_weight, current_value):
    global max_wieght
    if current_weight > max_weight:
        return float("-inf")
    
    if current_weight == max_weight:
        return current_value
    
    if cursor >= num_stuffs:
        return float("-inf")
    
    _max = -1
    _max = max(find_max(cursor + 1,
                        current_weight + stuffs[cursor][0], 
                        current_value + stuffs[cursor][1]), 
                find_max(cursor + 1, current_weight, current_value))
    
    return _max

def find_max2(cursor, current_weight):
    global max_wieght
    if current_weight > max_weight:
        return float("-inf")
    
    if current_weight == max_weight:
        return 0
    
    if cursor >= num_stuffs:
        return float("-inf")
    
    _max = -1
    _max = max(find_max2(cursor + 1,
                        current_weight + stuffs[cursor][0]) + stuffs[cursor][1], 
                find_max2(cursor + 1, current_weight))
    
    return _max

dp = [[-1 for _ in range(max_weight)] for _ in range(num_stuffs)]
def find_max3(cursor, current_weight):
    global max_wieght
    if current_weight > max_weight:
        return float("-inf")
    
    if current_weight == max_weight:
        return 0
    
    if cursor == num_stuffs:
        return 0 
    
    if dp[cursor][current_weight] != -1: # 이미 계산한 값은 계산 안하게 바로 리턴
        return dp[cursor][current_weight]
    
    _max = -1
    _max = max(find_max3(cursor + 1,
                        current_weight + stuffs[cursor][0]) + stuffs[cursor][1], 
                find_max3(cursor + 1, current_weight))
    
    dp[cursor][current_weight] = _max
    return dp[cursor][current_weight]
print(find_max3(0, 0))