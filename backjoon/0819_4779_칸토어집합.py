
def solve(n):
    if n == 1:
        return "-"

    left = solve(n // 3)
    center = " " * (n // 3)
    return left + center + left

while True:
    try:
        N = int(input())

        result = solve(3 ** N)
        print(result)
    except:
        break

# solve(27) -> n = 27 (solve(9)), left = '- -   - -', center = '         ', return = '- -   - -         - -   - -'
# solve(9) -> n = 9 (solve(3)), left = '- -', center = '   ', return '- -   - -'
# solve(3) -> n = 3 (solve(1)), left = '-', center = ' ', return '- -'
# solve(1) -> return '-'