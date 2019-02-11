# coding = utf-8
import re
"""
1. . 匹配任意字符(一个点代表一个占位符，两个点代表两个占位符,如果类推...)，换行符（\n）除外
2. * 匹配前一个字符0次或无限次
3. ? 匹配前一个字符0次或1次
4. .* 贪心算法
5. .*? 非贪心算法
6. () 括号内的数据作为结果返回
"""

# .的使用例子
a = 'xy12xy3'
b = re.findall('x.', a)
print(b)

# *的使用例子
a = 'xy12xy3'
b = re.findall('x*', a)
print(b)

# ?的使用例子
a = 'xy12xy3'
b = re.findall('x?', a)
print(b)

# .* 使用例子
a = 'laodhfejzuwxyzixyzladivhwanxyzlovexyzawidhlxyzpythonxyzasdwia'
b = re.findall('xyz.*xyz', a)
print(b)

# .？使用例子
a = 'laodhfejzuwxyzixyzladivhwanxyzlovexyzawidhlxyzpythonxyzasdwia'
b = re.findall('xyz.*?xyz', a)
print(b)

# ()使用例子
a = 'laodhfejzuwxyzixyzladivhwanxyzlovexyzawidhlxyzpythonxyzasdwia'
b = re.findall('xyz(.*?)xyz', a)
print(b)

# 换行符的处理（\n）
a = '''sdfxxhello
xxfsdfxxworldxxasdf'''
# b = re.findall('xx(.*?)xx', a)
b = re.findall('xx(.*?)xx', a, re.S)
print(b)

# 匹配数字推荐使用(\d+)
a = 'abc123cdf5555fffadc'
b = re.findall('(\d+)', a)
print(b)

""" 
--------------------------------
总结：匹配字符使用(.*?),匹配数字使用(\d+)
--------------------------------
"""