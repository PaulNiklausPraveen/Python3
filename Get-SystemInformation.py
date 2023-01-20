import socket
import psutil
import multiprocessing
import datetime
import os
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
ram=psutil.virtual_memory().total/1000000000
print("Hostname: ",hostname)
print("IP Address: ",ip_address)
print("System RAM (GB):",int(ram))
print("RAM memory % used:", psutil.virtual_memory()[2])
print("CPU Count: ", multiprocessing.cpu_count())
print("System started at:", datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%H:%M:%S %Y-%m-%d"))
