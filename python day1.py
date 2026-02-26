name = input("你的名字：")
age  = input("你的年龄：")
city = input("你的位置：") 

print("\n ============== ")
print("我是",name)
print("年龄",age)
print("位置",city)
print("\n ==============")

A1 = int(input("数字一："))              #加法数学计算
A2 = int(input("数字二："))

#计算输出
A3 = A1 + A2
print(A3)

# 摄氏度转华氏度：F = C × 1.8 + 32
C = float(input("请输入摄氏度"))
F = C * 1.8 + 32
print(F"华氏度")

print("简易计算器")
print("1.加  2.减  3.乘  4.除")






age = int(input("你的年龄"))

if age >= 18:
    print("参加")
elif age > 10:
    print("可以参加但是需要家长监督")
else:
    print("不可以参加问卷")

print("简易计算器")
print("+ - * / ")

choice = input(" + - * / ")
N1 = int(input("数字一"))
N2 = int(input("数字二"))

if choice == "+":
    print("结果:", N1+N2)
elif choice == "-":
    print("结果：", N1-N2)
elif choice == "*":
    print("结果：", N1*N2)
elif choice == "/":
    if N2 !=  0:
        print ("结果：", N1/N2)
    else:
        print("错误不能除0")
else:
    print("错误")

for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j}*{i}={j*i}",end="\t")
    print()
