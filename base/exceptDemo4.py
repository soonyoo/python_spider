# coding = utf-8

try:
    # 1.提示输入一个整数
    num = int(input('请输入数字：'))
    # 2.使用8除以用户输入的整数并输出
    result = 8/num
    print(result)
except ValueError:
    print('wrong:输入的数值类型有误！请输入整数类型')
except Exception as result:
    print('wrong:获取未知错误：%s' % result)
else:
    print('没有异常才会执行的代码')
finally:
    print('无论是否有异常，都会执行的代码！')
