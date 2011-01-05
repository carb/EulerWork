'913 * 993 = 906609'

global palindrome
palindrome = [0,0]
for num1 in range(100,1000):
  for num2 in range(100,1000):
    num = num1 * num2
    numstr = '%s' % (num)
    if len(numstr) == 6:
      front = numstr[:3]
      back = numstr[5] + numstr[4] + numstr[3]
      if front == back and (palindrome[0]*palindrome[1])<(num1*num2):
        palindrome = [num1, num2]

print palindrome[0], "*", palindrome[1], " = ", palindrome[0]*palindrome[1]


'max([x*y for x in range(900,1000) for y in range(900,1000) if str(x*y) == str(x*y)[::-1]])'
