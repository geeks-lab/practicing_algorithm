jemini = list(map(int, input().split()))
guli = list(map(int, input().split()))

j_score, g_score = 0, 0
jemini_is_winning = False
for i in range(9):
    j_score += jemini[i]
    if j_score > g_score:
        jemini_is_winning = True
    g_score += guli[i]

if j_score < g_score and jemini_is_winning is True:
    print('Yes')
else:
    print('No')