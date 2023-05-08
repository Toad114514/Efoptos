"""
Copyright 114514 Toad114514

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

 http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import os

print("_____l         _______     ")
print("______l       /_ins__/l      ")
print("l______l      l o o l l")
print(" l______l     l ___ l l")
print("  l______l    l_____l／     ")
print("state3 install center (ver.23w01a)")
input("回车继续...")
os.system("clear")
while 1:
    print("_______________________________")
    print("     state3 安装中心           ")
    print("     1. 安装 proot          ")
    print("2. 安装 chroot(手机root建议)")
    print(" 3. 安装桌面(proot/chroot)")
    print("    4. 安装 EfoptOS 各种版本")
    print("        5. 退出")
    print("_______________________________")
    sel = input("""输入选择的数字[1-5])
_______________________________""")
    if sel == 1:
        os.system("python3 ~/EfoptOS/state3/proot.py")
    if sel == 2:
        os.system("python3 ~/EfoptOS/state3/chroot.py")
    if sel == 3:
        os.system("python3 ~/EfoptOS/state3/desktop.py")
    if sel == 4:
        os.system("python3 ~/EfoptOS/state3/einst.py")
    if sel == 5:
        break