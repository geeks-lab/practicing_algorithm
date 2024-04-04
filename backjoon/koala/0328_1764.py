n, m = map(int, input().split())

never_heard = set()
never_heardnseen = []

for i in range(n):
    never_heard.add(input())

for i in range(m):
    checking = input()
    if checking in never_heard:
        never_heardnseen.append(checking)

print(len(never_heardnseen))
for i in sorted(never_heardnseen):
    print(i)
