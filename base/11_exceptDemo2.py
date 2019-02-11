# coding = utf-8

# # 1.提示输入一个整数
# num = int(input('请输入数字：'))
# # 2.使用8除以用户输入的整数并输出
# result = 8 / num
# print(result)

try:
    # 1.提示输入一个整数
    num = int(input('请输入数字：'))
    # 2.使用8除以用户输入的整数并输出
    result = 8/num
    print(result)
except ValueError:
    print('wrong:输入的数值类型有误！请输入整数类型')
except ZeroDivisionError:
    print('wrong:除0错误！')
