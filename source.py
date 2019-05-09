pn=[2]
A=int(input("数字を入力してください(この数字以下の素数を表示します)："))
PN=int(input("素数かどうか調べたい数を入力して下さい:"))
for List in range(3,A):
    chk=True
    for L2 in pn:
        if List%L2 == 0:
            chk=False
    if chk==True:
        pn.append(List)
print(pn)

if PN in pn:
    print("素数です")
else:
    print("合成数です")
