import os

print('''
EfoptOS 帮助 v1.3 命令行模式
 - 输入 help-tui 进入帮助中心TUI模式(测试)
 - 帮助随安装包安装后改变，将加入该安装的简单帮助及命令。
''')
helpdoc = open('help.con', 'r')
print('''
''')
strding = helpdoc.read()
print(strding)
helpdoc.close()