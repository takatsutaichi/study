import math

n=int(input("数字を入力してください:"))
def pjudge(num):
    divisor=int(math.sqrt(n))
    for i in range(2,divisor):
        if n%i==0:
            print(str(num)+"は合成数です")
        else:
            print(str(num)+"は素数です")

pjudge(n)
