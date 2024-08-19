"""
Copyright 2023 Toad114514

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

 http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

(上方是apache2.0开源协议，禁止违反协议）
EfoptOS是一个在termux、Zerotermux和Utermux上运行的一个OS System系统。因为用来练手，所以代码肯定烂大街。
预计1年内做完，做完后可以去github或gitee上提建议或提bug。
"""


import os
import time
import datetime
import getpass
import sqlite3

print("              ")
print("    ---\     _____l           ")
print("   ｜   \       o l        ")
print("    ---  \   o    l         ")
print("   ｜     \   l/  l         ")
print("    ---    \ /\   l           ")
print("              EfoptOS b1.0 copyright 2023 Toad114514")
input("输入任意东西继续")
while 1:
    print("""
公告：
1 终端
2 Fget Panel
3 state3安装器
4 tmoe菜单（高阶）
5 VS code web
6 Letchat
7 更新（git、wget和dpkg)
8 新建proot启动脚本到home
9 config和termux美化
10 仿minecraft-pocket服务器
11 vnc设置
12 退出菜单
    	""")
    sel=input("输入编号执行")
    if sel == "1":
        os.system("zsh")
    if sel == "2":
        os.system("python3 ~/EfoptOS/panel/start.py")
    if sel == "3":
        os.system("python3 ~/EfoptOS/state3/install.py")
    if sel == "12":
        break