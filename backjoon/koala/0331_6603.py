import sys
input = sys.stdin.readline

def dfs(lotto, nums, visited):
    if len(lotto) == 6:
        for i in range(6):
            print(nums[lotto[i]], end=' ')
        print()
        return

    temp_visited = visited[:]
    for i in range(len(temp_visited)):
        if not temp_visited[i]:
            temp_visited[i] = True
            dfs(lotto + [i], nums, temp_visited)


while True:
    a_line_of_nums = list(map(int, input().split()))
    if len(a_line_of_nums) == 1 and a_line_of_nums[0] == 0:
        break

    length = a_line_of_nums.pop(0)

    visited = [False] * len(a_line_of_nums)
    dfs([], a_line_of_nums, visited)