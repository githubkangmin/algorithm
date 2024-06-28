n = int(input())


for i in range(n):
    score = 0
    tscore = 0
    ox = input()
    for j in range(len(ox)):
        if ox[j] == 'O':
            score += 1
        else:
            score =0
        tscore += score
    print(tscore)