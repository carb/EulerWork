numrange = range(1000000, 0, -1)
best = 0
bestscore = 0
for num in numrange:
  score = 0
  tempnum = num
  while num != 1:
    if num%2 == 0: num /= 2
    else: num = 3*num + 1
    score += 1
  if score > bestscore:
    bestscore, best = score, tempnum
    print bestscore, best

