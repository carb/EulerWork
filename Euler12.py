def factor(number):
  from math import sqrt
  factors = []
  if sqrt(number)==int(sqrt(number)):
    return [1]
  for i in range(1,int(sqrt(number))):
    if number%i==0:
      factors.append(i)
  return factors*2

def main():
  count,sum,facts = 1,0,[]
  while len(facts)<=500:
    sum += count
    facts=factor(sum)
    count+=1
  return sum



