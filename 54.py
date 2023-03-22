import time
st = time.time()
l=[]
n = 40
def fibb(n):
   if n <= 1:
       return n
   else:
       return(fibb(n-1) + fibb(n-2))
if n <= 0:
   print("blad")
else:
   for i in range(n):
       l.append(fibb(i))
print(l)

et = time.time()
elapsed_time = et - st
print('Execution time:', time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))