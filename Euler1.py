total = []
total = range(1000)
for num in range(1000):
  if (num%3 == 0):
    total[num] = num
  elif (num%5 == 0):
    total[num] = num
  else:
    total[num] = 0
print sum(total)
