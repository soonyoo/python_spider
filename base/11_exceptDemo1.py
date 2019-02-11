# coding = utf-8

# demo1 简单的捕获异常语法

try:
    input_val = int(input('请输入数字：'))
    print('您输入的是%d' % input_val)
except:
    print('wrong:您输入的不是数值类型')

print('-'*30)


