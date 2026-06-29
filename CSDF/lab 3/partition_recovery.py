import os
import subprocess
import sys

print("Partition Recovery Script")
print("List of devices attached to system is:")
os.system("lsblk")

devname = input("Enter the device name: ")
if not devname.strip():
    print("Error: Device name cannot be empty.")
    sys.exit(1)

dev_path = f"/dev/{devname}"
if not os.path.exists(dev_path):
    print(f"Error: Device '{dev_path}' does not exist.")
    sys.exit(1)

# Show the list of partitions
print("Showing partition table:")
ret = subprocess.run(
    f'echo -e "p\nq\n" | sudo fdisk {dev_path}',
    shell=True, capture_output=True, text=True
)
if ret.returncode != 0:
    print(f"Error: Failed to read partition table. {ret.stderr}")
    sys.exit(1)
print(ret.stdout)

pno = input("Enter the partition number to recover: ")
if not pno.strip():
    print("Error: Partition number cannot be empty.")
    sys.exit(1)

# Recover the partition
ret = subprocess.run(
    f'echo -e "n\n\n{pno}\n\n\nw\n" | sudo fdisk {dev_path}',
    shell=True, capture_output=True, text=True
)
if ret.returncode != 0:
    print(f"Error: Failed to recover partition. {ret.stderr}")
    sys.exit(1)

print("Partition recovery completed successfully.")