n   = int(input("数字を入力してください："))

x=0
for a in range(1,n+1):
    result = n%a
    if result == 0:
        x+=1
    else:
        x+=0

if x == 2:
    print(str(n)+"は素数です")
else:
    print(str(n)+"は素数ではありません")


