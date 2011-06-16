def isprime(n):
  n=abs(int(n))
  if n<2:
    return False
  if n==2:
    return True
  if not n&1:
    return False
  for x in range(3, int(n**0.5)+1,2):
    if n%x == 0:
      return False
  return True

bestnab=[0,0,0]

for a in range(-999,1000):
  print bestnab
  for b in range(-999,1000):
    n,m=0,5
    while isprime(m):
      m = (n**2)+a*n+b
      if n>bestnab[0]:
        bestnab[0]=n
        bestnab[1]=a
        bestnab[2]=b
      n+= 1

#a,b,m,n=-79,1601,5,0
#while isprime(m):
#  m=(n**2)+a*n+b
#  print n,m,isprime(m)
#  n+=1


print "a = ",bestnab[1]
print "b = ",bestnab[2]
print bestnab[1]*bestnab[2]
