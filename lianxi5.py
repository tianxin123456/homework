temp = input('请输入一个非负整数：')
num = int(temp)

result = []

def DectoBin(dec):
    bin = ''
    if dec:
        bin = DectoBin(dec//2)
        return bin + str(dec % 2)
    else:
        return bin

for i in range(0, num+1):
    count = 0
    #a = bin(i)  #此时a应该是个以0b开头的字符串 eg:'0b10'
    #str1 = a[2:] #去掉不必要的0b str1是一串二进制数字的字符串
    str1 = DectoBin(i)
    for j in str1:
        if j == '1':
            count += 1
    result.append(count)
print(result)






