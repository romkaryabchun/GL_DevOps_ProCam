# GL_DevOps_ProCam
The script written using python and uses psutil library. The script has three functions and has 1 argument as an input.
Function `get_serv_memory()` prints general information on memory.
Function `get_serv_cpu()` prints general CPU information.
And function `get_serv_process()` prints general information on running process.
If the argument is not set - prints error message.

#### Example 

`python3 sysinfo.py cpu`

**Output:** 

```
Get information about CPU
user  =  1528.61
nice  =  2.14
system  =  24950.3
idle  =  197292.26
iowait  =  375.49
irq  =  0.0
softirq  =  29.02
steal  =  0.0
guest  =  0.0
guest_nice  =  0.0
```
### Dockerfile

**sysinfo 0.0.4**
The container has the Python v3 script running. When the container starts, it prints out information about processes running on the host machine from within container environment

### Getting Started
In order to run container, you will need docker installed

### Usage
Docker container public view: https://hub.docker.com/r/romkaryabchun/sysinfo
**Run**

Run the container in the following way:

`docker run --rm -v /proc/:/proc/ romkaryabchun/sysinfo:0.0.4 mem`

`docker run --rm -v /proc/:/proc/ romkaryabchun/sysinfo:0.0.4 cpu`

`docker run --rm -v /proc/:/proc/ romkaryabchun/sysinfo:0.0.4 proc`

**Built With**

  -Python v3.5.3
  -psutil v5.6.2

**Auhtor**
Roman Ryabchun
