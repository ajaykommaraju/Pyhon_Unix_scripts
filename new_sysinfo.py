#script to reuse the code block from other program
#!/usr/dev_infra/platform/bin/python2.7
from sysinfo_func2 import disk_func
import subprocess

def network_info():
    ipaddr = "ifconfig"
    ipaddr_args = "-a"
    print " Ip address of the machine is :"
    subprocess.call([ipaddr, ipaddr_args])

def main():
    disk_func()
    network_info()

if __name__ == "__main__":
    main()
