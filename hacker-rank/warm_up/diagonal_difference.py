def diagonalDifference():
    size = int(input())
    thematrix = []
    firstdiag = []
    seconddiag = []
    for i in range(size):
        line = input().strip().split(' ')
        line = [int(j) for j in line]
        thematrix.append(line)
    for i in range(size):
        firstdiag.append(thematrix[i][i])
        seconddiag.append(thematrix[i][(size - 1) - i])
    print('the abs : ', abs(sum(firstdiag) - sum(seconddiag)))


diagonalDifference()

