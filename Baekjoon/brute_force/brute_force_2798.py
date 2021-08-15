from itertools import combinations

num, target = map(int, input().split())
s = [int(n) for n in input().split()]

# combinations을 이용해 모든 순서쌍 조합
combination = list(combinations(s, 3))

sum_comb = []

for i in range(len(combination)):
    sum_comb.append(sum(combination[i]))

result = list(sorted(set(sum_comb)))

for i in range(len(result)):
  flag = False
  if (result[i] == target):
    print(result[i])
    break
  elif (result[i] > target):
    print(result[i-1])
    break
  
  flag = True

if flag:
  print(result[-1])