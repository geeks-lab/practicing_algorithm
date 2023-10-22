#9498 시험 성적

grade = int(input())

if grade in range(90, 101):
    print('A')
elif grade in range(80, 91):
    print('B')
elif grade in range(70, 81):
    print('C')
elif grade in range(60, 71):
    print('D')
else:
    print('F')