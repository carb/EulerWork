#!usr/bin/python
numwords = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety'}
sum1 = 0
for i in range(1000):
 total = ''
 if 0<i<20:
  total+=numwords[i]
 elif 20<=i<100:
  i1 = (i/10)*10
  total+=numwords[i1]
  i2 = i-i1
  if i2 != 0:
   total+=numwords[i2]
 elif i>=100:
  i1 = (i/100)
  total+=numwords[i1]
  total+='hundred'
  i2 =  i-i1*100
  i3 =    i2/10
  i4 = i2-i3*10
  if i3 != 0 or i4 != 0:
   total+='and'
  if i3==1:
   total+=numwords[i3*10+i4]
  else:
   if i3 != 0:
    total+=numwords[i3*10]
   if i4 != 0:
    total+=numwords[i4]
 sum1+=len(total)

print sum1
