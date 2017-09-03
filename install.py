import os

package_name = input("enter Package name: ")

command = "pip3 --proxy 127.0.0.1:1990 install " + package_name.rstrip()
print(command)
os.system(command)
