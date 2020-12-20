import math
def IsPrime(n):

    flag = True
    #判断是否为质数
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0 :
            flag = False
            break
    return flag

def demo(n):
    if n > 0 and n%2 == 0 :
        #利用二分法找出小于n/2的素数(由二分法可知，
        #若两素数之和等于n
        #则其中较小的素数一定小于或等于n/2)
        for i in range(int(n/2)+1):
            if IsPrime(i) and IsPrime(n-i) :
                #函数的调用（实参与形参的对应）
                print(n,'=',i,'+',n-i)
def main():
    a = int(input("请输入一个正偶数"))
    demo(a)
#程序入口
if __name__ == '__main__':
    main()
