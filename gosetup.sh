#!bin/sh
echo -----------
echo EfoptOS 安装向导
echo ----------
echo 正在安装环境和依赖...
apt install python3 git aria2 curl wget
echo 正在调整环境...
echo 克隆仓库
git clone https://github.com/toad114514/efopt.git
echo 安装完成，现在可以通过输入eos.sh启动。
