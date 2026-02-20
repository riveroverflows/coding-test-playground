n = int(input())
s = input()

answer = 0

for i in range(n):
    if s[i] != "A":
        continue
    a_cnt = 0
    n_cnt = 0
    for j in range(i + 1, n):
        if j >= i + 2 and s[j] == "A" and a_cnt == 0 and n_cnt == 1:
            answer += 1
        if s[j] == "A":
            a_cnt += 1
        if s[j] == "N":
            n_cnt += 1

print(answer)
