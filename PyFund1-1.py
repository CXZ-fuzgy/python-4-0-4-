物料 = []

while True:
    name = input("请输入物料序列号（输入q结束）")
    if name=="q":
        break
    age = input(f"请输入物料{name}在库时间")

    物料信息 = [name,int(age)]
    物料.append(物料信息)


print("\n所以物料信息如下")
for 物料信息 in 物料:
    编号 = 物料[0]
    在库时间 = [1]

    if 在库时间 > 10:
        状态 = '回收'
    else :
        状态 = '使用'
    print(f'编号:{编号},在库时间:{在库时间},状态：{状态}')
