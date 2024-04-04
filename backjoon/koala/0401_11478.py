input_string = input()

cnt = set()
for i in range(len(input_string)):
    for j in range(i, len(input_string)):
        cnt.add(input_string[i:(j+1)])

print(len(cnt))
