def makeStars(n):
  if n == 1:
    return ['*']

  starList = makeStars(n//3)
  list = []

  for star in starList:
    list.append(star*3)
  for star in starList:
    list.append(star+' '*(n//3)+star)
  for star in starList:
    list.append(star*3)
    
  return list

N=int(input())
print('\n'.join(makeStars(N)))

# r(27)
# r(9)
# r(3) n = 3, stars = ['*'], 1forloop list = ['***'], 2forloop list = ['***', '* *'], 3forloop list = []
# r(1) -> return ['*']