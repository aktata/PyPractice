# TempConvert.py
def main():
    temp_str = input("请输入带有符号的温度值: ")
    if temp_str[-1] in ['F', 'f']:
        c = (eval(temp_str[0:-1]) - 32) / 1.8
        print("转换后的温度是{:.2f}C".format(c))
    elif temp_str[-1] in ['C', 'c']:
        f = 1.8 * eval(temp_str[0:-1]) + 32
        print("转换后的温度是{:.2f}F".format(f))
    else:
        print("输入格式错误")


if __name__ == '__main__':
    main()
