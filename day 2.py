a=int(input('enter the number up to which u want a pattern: '))
for i in range(1, a+1):
 print(" "* (a-i) ,str(i)*i)