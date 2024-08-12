#Finding a time to execute the code 
import time 
start = time.time()
for i in range(1,101):
    print(i)
print(time.time()-start)