fibseq = [1,2]
fibeven = [2]
for num in range(10000)[2:]:
  fibseq += [0]
  fibseq[num] = fibseq[num-1] + fibseq[num-2]
  if (fibseq[num] % 2 == 0):
    fibeven += [fibseq[num]]
  if fibseq[num]>4000000:
    break
print fibeven
print sum(fibeven)
