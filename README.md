# EfoptOS
Toad114 开发的 python 环境仿终端+系统程序
## 停更
😭本仓库已停更！😭个人不打算再进行该仓库的更新工作！Goodbye EfoptOS😭😭😭😭😭但我们还有Staxle🤣

#### 特点及未来特性
 - √ 类console界面
 - √ 支持各种Linux发行版、termux及魔改的ut和zt
 - √ bash/python 安装器
 - 自带常用软件
  - EPlayer 播放器
  - Ernet 浏览器
  - ...
 - 自带自制 EfoptOS Package Explorer
 - 自带 NiceGUI/Pywebio 网站远程管理面板
 - 快速安装使用高级Linux菜单(例如tmoe-linux)
 - 通过 Proot/Chroot 容器快速安装发行版Linux
 - √ 部分软件提供 TUI 界面
 - 快速部署 Nginx/Apache 服务器
 - 自制软件开发 API 插件
 - pkg/apt/yum/pacman/epk 已被TUI化
 - SuperQemu TUI/GUI/Web 化虚拟机管理面板
 - Desin-shop 基于Git商店，允许切换仓库
 - 自动更新
 - ...

#### 和flyos有什么区别？
- 遵循协议，不违法协议
- 代码大部分自写
- 比flyos更多的功能
- ...

#### 安装
**部署EfoptOS环境**
在termux/proot/chroot安装git和python3
已安装可以升级
```
pkg update
```
未安装输入
```
pkg install git python
```
然后输入

```
git clone https://gitee.com/toadstool/efopt.git
```
要走过场的话，就输入
```
python3 install.py
```
不想就输入
```
efopt.sh
# 如果没用请使用下面代码
source efopt.sh
```

结束了，别看了
