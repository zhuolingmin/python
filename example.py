num1 = int(input('num1 : '))
num2 = int(input('num2 : '))
#两个数中较小的一个
min_num = min(num1, num2)
#最大公约数的范围在1-min_num之间，
#最大公约数就是num1和num2能整除的最大的数
for i in range(1, min_num + 1):
    if num1 % i == 0 and num2 % i ==0:
        gys = i
#最小公约数
lcm = int((num1 * num2)/gys)
print('%s 和 %s 的最大公约数为 %s'%(num1, num2, gys))
print('%s 和 %s 的最小公约数%s' %(num1, num2, lcm))
