# 2675 문자열 반복

# 입력 값 잘못 이해하고 짠 코드
def myfunction(S, R):
    # 문자열 S를 R번 반복하여 새 문자열 P만들기
    splited_string_list = list(S)
    print(splited_string_list)

    P = []
    for letter in splited_string_list:
        for i in range(R):
            P.append(letter)
        
    #리스트 원소들을 합쳐서 하나의 string으로 -> ''.join(a)
    print(''.join(P))
myfunction('Happy',3)


def myfunction2():
    # 문제 : 문자열 S를 R번 반복하여 새 문자열 P만들기
    # 입력 : 2\n 3 ABC\n 5 HAP
    N = int(input()) # 총 몇개
    R, S = (input().split()) # 반복 횟수, 문자열
    
    S = list(S)
    temp_list = []

    for letter in S:
        for _ in range(int(R)):
            temp_list.append(letter)
    
    #리스트 원소들을 합쳐서 하나의 string으로 -> ''.join(a)
    P = ''.join(temp_list)
    print(P)

def developed():
    # list 안쓰고 * 연산자 사용하기

    Case = int(input()) # 총 몇개

    for _ in range(Case):
        R, S = input().split()
        for j in range(len(S)):
            print(S[j] * int(R), end='')
        print('')

developed()



