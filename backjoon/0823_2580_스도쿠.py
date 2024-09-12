array = []
zeroCnt = 0

for i in range(9):
    list1 = list(map(int, input().split(' ')))
    for e in list1:
        if e == 0:
            zeroCnt += 1
    array.append(list1)

def is_valid(x, y, num):
    global array
    for i in range(9):
        if array[x][i] == num or array[i][y] == num:
            return False
    start_x, start_y = 3 * (x // 3), 3 * (y // 3)
    for i in range(3):
        for j in range(3):
            if array[start_x + i][start_y + j] == num:
                return False
    return True

def solve_sudoku():
    global array, zeroCnt
    for i in range(9):
        for j in range(9):
            if array[i][j] == 0:
                for num in range(1, 10):
                    if is_valid(i, j, num):
                        array[i][j] = num
                        zeroCnt -= 1
                        if solve_sudoku():
                            return True
                        array[i][j] = 0
                        zeroCnt += 1
                return False 
    return True

solve_sudoku()

for row in array:
    print(' '.join(map(str, row)))
