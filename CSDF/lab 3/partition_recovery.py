import os
print("Partion Recovery Script")
print("List of devices attached to system is")
os.system("lsblk")
devname = input("Enter the device name\n")

#show the list of partition
commandline = 'echo -e "p\nq\n" | sudo fdisk /dev/'+devname
print("Showing partition table")
os.system(commandline)

pno = input("Enter the partition no to recover ")

#delete the partition
commandline='echo -e "n\n\n' + pno +'\n\n\nw\n" | sudo fdisk /dev/'+devname
os.system(commandline)