#-*-coding:utf8;-*-
#qpy:2
#qpy:console
import os

print("----------------------------")
print("EEE  ff           t  OOO SSS")
print("E    f           ttt O O S")
print("EEE fff ooo  ppp  t  O O SSS")
print("E    f  o o  p p  t  O O   S")
print("EEE  f  ooo  ppp  tt OOO SSS")
print("    ff       p")
print("             p")
print("----------------------------")
print("EfoptOS install center 安装向导")
input("输入任意键继续...")
fazvar=open("/sdcard/faz.txt","r")
if (fazvar == "efoptosinstalls...[580987]"):
    print("[error:001]faz.txt限制安装。")
else:
    yonins = input("是否安装EfoptOS?[y/n/t]")
    if yonins == "y":
        print("正在安装。。。")
        bj=open("/sdcard/faz.txt","w+")
        bj.write("efoptosinstalls...[580987]")
        bj.close()
        print("安装pkg包...")
        os.system("pkg install git wget apt unzip unrar vi vim curl")
        print("安装完成。输入~/EfotpOS/efopt.sh即可")