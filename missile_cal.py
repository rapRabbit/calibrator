import math

if __name__ == '__main__':
    print('***欢迎使用发弹模拟系统***')
    total = input('请输入该轮模拟发射导弹总数: ')
    total = int(total)
    print('请输入首发导弹坐标')
    a1, b1 = map(int, input().split(","))
    print("首发导弹坐标为：" + str(a1) + ',' + str(b1))
    print('请输入第二发导弹坐标')
    a2, b2 = map(int, input().split(","))
    print("第二发导弹坐标为：" + str(a2) + ',' + str(b2))
    a = round((1 / 2) * (a2 - a1) + a1, 4)
    b = round((1 / 2) * (b2 - b1) + b1, 4)
    print("当前平均弹着点为：" + str(a) + ',' + str(b))
    pre_len = math.sqrt(((a - a2) ** 2) + ((b - b2) ** 2))
    #print(pre_len)
    num = 3
    while num <= total:
        print('请输入第' + str(num) + '发导弹坐标')
        x, y = map(int, input().split(","))
        cur_len = math.sqrt(((x - a) ** 2) + ((y - b) ** 2))
        #print(cur_len)
        if (pre_len * 2 + 0.000001) >= cur_len:
            a = round((1 / num) * (x - a) + a, 4)
            b = round((1 / num) * (y - b) + b, 4)
            print('第' + str(num) + '发导弹坐标为：' + str(x) + ', ' + str(y))
            print("当前平均弹着点为：" + str(a) + ',' + str(b))
            num += 1
            pre_len = cur_len
        else:
            print("导弹已偏离！！！")
            break
    print('本轮模拟结束')
