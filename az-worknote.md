#### Export/Inport python package
```
$ pip freeze > requirements.txt
$ pip install -r requirements.txt
```
#### Ubuntu show Nvidia gpu status
```
$ pip install gpustat
$ gpustat -cp
```
#### Count text file rows
``` 
$ wc -l vocab_kehuan.txt
17301 vocab_kehuan.txt

$ wc -l train-kehuan-utf8.json
7057809 train-kehuan-utf8.json
```

#### Show Nvidia GPU status
```
$ pip install gpustat
$ gpustat -cp
```

#### list file size
```ls -lh
-rw-r--r-- 1 root root  16M 10月 16 02:23 train-doupo.json
-rw-r--r-- 1 root root 747M 10月 16 19:08 train-kehuan-utf8.json
```

#### Mac os comman
top: show running processes, memory usage and similar stats
iostat: show I/O per terminal, device and SPU summery statistics
vm_stat: show Mach virtual memory statistics
df and diskutil list: report on drive space used and free
fs_usage: show file activity for both disk and network
nettop: display updated information about the network (a bit like top for net I/O)
w: display who is logged in, what they are doing and system load
ifconfig and ipconfig: network interface and IP protocol details
