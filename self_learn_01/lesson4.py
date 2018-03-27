# schedule
time.time(); time.sleep(2); time.time()


# python 无异步
# 但可同时跑多个进程

# 生男生女

import random


def boy_girl(n):
    sum_g = 0
    sum_b = 0
    rate = 0
    for i in range(n):
        g=0
        b=0 #p_girl = random.randint(0,1)
        while random.randint(0,1) == 1:
            g = g+1
        
        b = b+1
        sum_g = sum_g+g
        sum_b = sum_b+b
        rate =  sum_g / (sum_g + sum_b)
    
    print("boy_number：" + str(sum_b))
    print("girl_number：" + str(sum_g))
    print("all children：" + str(sum_b+sum_g))
    print("rate of girl：" + str(rate))


boy_girl(3)

n=5

for i in range(n):
    g=0
    b=0 #p_girl = random.randint(0,1)
    while random.randint(0,1) == 1:
        g = g+1
     
    b = b+1
    sum_g = sum_g+g
    sum_b = sum_b+b
    rate =  sum_g / (sum_g + sum_b)

print("boy_number：" + str(sum_b))
print("girl_number：" + str(sum_g))
print("all children：" + str(sum_b+sum_g))
print("rate of girl：" + str(rate))
