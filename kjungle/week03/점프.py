
num_rocks = 0
def jump(c, r):
    if c > num_rocks:
        return 214748
    
    if c == num_rocks:
        return 0
    
    _min = 214748

    if c + r not in set and r != 0:
        return min(jump(c+r,r)+1, _min)
    
    if c+r+1 not in set: # 속도1증가시
        return min(jump(c+r+1, r+1)+1, _min)

    if c+r-1 not in set and r > 1:
        return min(jump(c+r-1,r-1)+1, _min)
    
    return _min