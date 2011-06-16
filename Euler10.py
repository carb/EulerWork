def eras(n):
  siv=range(n+1)
  siv[1]=0
  sqn = int(round(n**0.5))
  for i in range(2,sqn+1):
    siv[2*i:n+1:i]=[0]*(n/i-1)
  return filter(None,siv)

primes = eras(2000000)
print sum(primes)
