#!/usr/bin/python
a,i='',0
while len(a)<=1000001:
 i+=1
 a+=str(i)
print int(a[0])*int(a[9])*int(a[99])*int(a[999])*int(a[9999])*int(a[99999])*int(a[999999])
