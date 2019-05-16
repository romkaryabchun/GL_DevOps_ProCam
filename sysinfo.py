import psutil, sys
def get_serv_memory():
    print("Get information about virtual memory and swap")
    virtual_mem = psutil.virtual_memory()
    swap_mem = psutil.swap_memory()
    for (key,value) in zip(virtual_mem._fields, virtual_mem):
        print("virtual", key, " = ", value)
    for (key1,value1) in zip(swap_mem._fields, swap_mem):
        print("swap",key1, " = ", value1)

def get_serv_cpu():
    print("Get information about the CPU")
    system_cpu = psutil.cpu_times(percpu=False)
    for (key,value) in zip(system_cpu._fields, system_cpu):
        print(key, " = ", value)

def get_serv_process():
    print("Getting information about the processes")
    processlist = [process.info for process in psutil.process_iter(attrs=['pid', 'name', 'username'])]
    for object in processlist:
        print('Name=', object['name'], " ", 'PID=', object['pid'], 'UserName=', object['username'])

try:
    if sys.argv[1] == 'mem':
        get_serv_memory()
    if sys.argv[1] == 'cpu':
        get_serv_cpu()
    if sys.argv[1] == 'proc':
        get_serv_process()
except IndexError:
    print("No parameter. Use one of the next parameters: 'mem' - to get info of memory, 'cpu' - to get info of system cpu or 'proc', to get info of process")
