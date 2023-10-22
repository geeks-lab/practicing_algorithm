# 2563 최대값

#9개의 서로 다른 자연수 중 최댓값을 찾고 그 최댓값이 몇 번째인지
def find_max():
    num_list = []
    for i in range(9):
        num_list.append(int(input()))
    # 최댓값 max함수로
    print(max(num_list))
    # 몇번째 인덱스였는지 index()함수로
    print(num_list.index(max(num_list))+1)