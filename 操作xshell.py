'''文件和目录管理
cd [directory]: 切换当前工作目录。
pwd: 显示当前工作目录。
ls [options]: 列出目录内容。
mkdir [directory]: 创建新目录。
rmdir [directory]: 删除空目录。
rm [options] [file]: 删除文件或目录（需小心使用）。
mv [options] [source] [destination]: 移动或重命名文件。
cp [options] [source] [destination]: 复制文件或目录。
ln [options] [source] [linkname]: 创建链接（硬链接或符号链接）。
chmod [options] [file]: 更改文件权限。
chown [options] [file]: 更改文件的所有权。
chgrp [options] [file]: 更改文件的组所有权。
find [path] [expression]: 在指定路径下查找文件。
locate [pattern]: 快速查找文件（需要预先运行 updatedb）。
文本处理
cat [file]: 显示文件内容。
more [file]: 分页显示文件内容。
less [file]: 可向前向后滚动地查看文件内容。
head [file]: 显示文件的前几行。
tail [file]: 显示文件的后几行。
grep [pattern] [file]: 在文件中搜索匹配指定模式的行。
sed [commands] [file]: 流编辑器，用于文本转换和过滤。
awk [script] [file]: 强大的文本处理工具。
cut [options] [file]: 从文件中切片输出选定的列。
sort [options] [file]: 对文件的内容排序。
uniq [options] [file]: 从文件中删除重复行。
tr [options] [file]: 替换或删除字符。
系统信息和监控
uname [option]: 显示系统信息。
uptime: 显示系统运行时间和用户登录信息。
date: 显示或设置系统日期和时间。
who: 显示当前登录的用户。
w: 显示谁登录以及他们正在做什么。
last: 显示登录记录。
top: 显示实时的系统资源使用情况。
htop: 类似 top，但提供了更多的功能和更好的界面。
ps [options]: 显示进程信息。
df [options]: 显示磁盘使用情况。
du [options] [file]: 估计文件或目录使用的磁盘空间。
free [options]: 显示系统内存使用情况。
netstat [options]: 显示网络连接和接口统计信息。
ifconfig [options]: 显示和配置网络接口。
ip [command]: 显示和操作网络设备、路由表等。
进程管理
kill [signal] [pid]: 发送信号给进程。
killall [signal] [command]: 发送信号给所有由 command 指定的进程。
nice [increment] [command]: 设置新进程的优先级。
renice [increment] [pid]: 改变进程的优先级。
网络工具
ping [host]: 测试网络连接。
traceroute [host]: 显示数据包到达目标主机所经过的路径。
nslookup [domain]: 查询域名系统的记录。
dig [domain]: DNS 信息查询工具。
curl [options] [URL]: 获取远程文件。
wget [options] [URL]: 从网络下载文件。
ssh [options] [user@host]: 安全登录远程主机。
scp [options] [source] [destination]: 安全复制文件。
sftp [options] [user@host]: 安全文件传输。
nc [options] [host] [port]: 网络调试和测试工具（netcat）。
软件包管理
apt [command] [package]: Debian 和 Ubuntu 系统中的软件包管理工具。
yum [command] [package]: CentOS 和 RHEL 系统中的软件包管理工具。
dnf [command] [package]: Fedora 和 RHEL 8+ 系统中的软件包管理工具。
pacman [command] [package]: Arch Linux 和其衍生发行版的软件包管理工具。
brew [command] [package]: macOS 的包管理器 Homebrew。
日志和调试
journalctl [options]: 查看系统日志。
dmesg: 显示内核消息。
strace [options] [command]: 跟踪系统调用和信号。
gdb [command]: GNU 调试器。
编辑器
nano [file]: 简单的文本编辑器。
vim [file]: 高级文本编辑器。
emacs [file]: 功能强大的文本编辑器。
其他
bash [script]: 运行 shell 脚本。
bashrc: Bash 的启动脚本。
bash_profile: 用户登录脚本。
cron [command]: 计划任务。
crontab [command]: 管理 cron 作业。
tar [options] [files]: 归档文件。
gzip [options] [file]: 压缩文件。
gunzip [options] [file]: 解压缩文件。
xz [options] [file]: 压缩文件。
unxz [options] [file]: 解压缩文件。
bzip2 [options] [file]: 压缩文件。
bzcat [options] [file]: 解压缩文件并显示内容。
man [command]: 查看命令的手册页。
info [command]: 查看命令的信息手册。
这个列表应该覆盖了大部分日常所需的功能，但根据具体的 Linux 发行版和环境，可用的命令可能会有所不同。如果你需要了解更多关于某个特定命令的信息，可以通过 man [command] 或 info [command] 来查看详细的帮助文档。'''