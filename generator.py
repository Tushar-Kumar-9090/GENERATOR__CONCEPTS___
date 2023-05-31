


## Question-1

#* Wap to print 1 to 10 by using generator?
def series(s,e,u=1):
    while s<e:
        yield s
        s+=u
s=series(1,10)
for i in s:
    print(i)







## Question-2
#* Wap to print Fibonacci series by using generator?


def fibo(fe,se,n):
    i=1
    while i<n:
        dummy=fe
        yield dummy
        fe=se
        se=dummy+fe
        i+=1
f=fibo(2,3,10)
for i in f:
    print(i)





#! 2nd method
def fibo(fe,se,n):
    i=1
    while i<n:
        yield fe
        fe,se=se,fe+se
        i+=1
f=fibo(2,3,10)
for i in f:
    print(i)









