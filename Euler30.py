#!/usr/bin/python

def decompInt(num):
  templist1 = list(str(num))
  templist2 = []
  for num2 in templist1:
    templist2.append(int(num2))
  return templist2

def fivePowerSum(lst):
  sum1 = 0
  for i in lst:
    sum1 += i**5
  return sum1
                               #the upper num was determined
fifthnums = []                 #by taking a six digit number 
for number in range(2,354295): #maximized: 6*(9**5) = 354294
  if number==fivePowerSum(decompInt(number)):
    fifthnums.append(number)

print fifthnums
print sum(fifthnums)
