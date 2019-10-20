### Cloud GPU Instance
Titan RTX 24G显存 E5-2680 v3 24核48G 1TB SSD + 4TB硬盘 网速D100/U20 (独占7.1元每小时) A

GTX 1080 Ti 四卡 E5-2640 v3 32核80G 700GB SSD + 4TB硬盘 网速D100/U20 (独占8元每小时)

tensorflow 1.14.0

python 3.6

### Export/Inport python package
```
$ pip freeze > requirements.txt
$ pip install -r requirements.txt
```
### Ubuntu show Nvidia gpu status
```
$ pip install gpustat
$ gpustat -cp
```
### Count text file rows
``` 
$ wc -l vocab_kehuan.txt
17301 vocab_kehuan.txt

$ wc -l train-kehuan-utf8.json
7057809 train-kehuan-utf8.json
```

### Show Nvidia GPU status
```
$ pip install gpustat
$ gpustat -cp
```

### list file size
```ls -lh
-rw-r--r-- 1 root root  16M 10月 16 02:23 train-doupo.json
-rw-r--r-- 1 root root 747M 10月 16 19:08 train-kehuan-utf8.json
```

### Mac os comman

top: show running processes, memory usage and similar stats

iostat: show I/O per terminal, device and SPU summery statistics

vm_stat: show Mach virtual memory statistics

df and diskutil list: report on drive space used and free

fs_usage: show file activity for both disk and network

nettop: display updated information about the network (a bit like top for net I/O)

w: display who is logged in, what they are doing and system load

ifconfig and ipconfig: network interface and IP protocol details

### Tar command
```
tar.gz
圧縮
tar -zcvf xxxx.tar.gz directory
解凍
tar -zxvf xxxx.tar.gz

tar.bz2
圧縮
tar -jcvf xxxx.tar.bz2 directory
解凍
tar -jxvf xxxx.tar.bz2

tar.xz
圧縮
tar -Jcvf xxxx.tar.xz directory
解凍
tar -Jxvf xxxx.tar.xz

tar
圧縮
tar -cvf xxxx.tar directory
解凍
tar -xvf xxxx.tar

zip
圧縮
zip -r xxxx.zip directory
解凍
unzip xxxx.zip
```
