def factor(number):
  from math import sqrt
  factors = [1]
  for i in range(2,int(sqrt(number+.5))+1):
    if number%i==0:
      factors.append(i)
      factors.append(number/i)
  return factors


def sumOfAmicableNumbers(number):
  total = []
  for i in range(number):
    sum1 = sum(factor(i))
    sum2 = sum(factor(sum1))
    if i==sum2 and i!=sum1:
      total.append(i)
  return sum(total)

