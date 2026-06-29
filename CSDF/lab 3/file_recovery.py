import os
import subprocess
import sys

os.system("clear")

print("File Recovery Script")
print("For Programing Wonders")
print("The list of devices is:")
os.system("lsblk")

devname = input("Enter the device to be used: ")
if not devname.strip():
    print("Error: Device name cannot be empty.")
    sys.exit(1)

imgname = input("Enter the image name: ")
if not imgname.strip():
    print("Error: Image name cannot be empty.")
    sys.exit(1)

ret = subprocess.run(["dd", f"if={devname}", f"of={imgname}", "bs=512"],
                     capture_output=True, text=True)
if ret.returncode != 0:
    print(f"Error: Failed to create disk image. {ret.stderr}")
    sys.exit(1)

print("Showing inode number of files:")
ret = subprocess.run(["fls", imgname], capture_output=True, text=True)
if ret.returncode != 0:
    print(f"Error: Failed to list files. {ret.stderr}")
    sys.exit(1)
print(ret.stdout)

inodeno = input("Enter the inode of the deleted file: ")
if not inodeno.strip():
    print("Error: Inode number cannot be empty.")
    sys.exit(1)

ret = subprocess.run(["istat", imgname, inodeno], capture_output=True, text=True)
if ret.returncode != 0:
    print(f"Error: Failed to get inode stats. {ret.stderr}")
    sys.exit(1)
print(ret.stdout)

print("The contents of the recovered file are:")
ret = subprocess.run(["icat", imgname, inodeno], capture_output=True, text=True)
if ret.returncode != 0:
    print(f"Error: Failed to recover file contents. {ret.stderr}")
    sys.exit(1)
print(ret.stdout)

newfile = input("Enter the name of the file where data to be stored (with extension): ")
if not newfile.strip():
    print("Error: File name cannot be empty.")
    sys.exit(1)

try:
    with open(newfile, 'w') as f:
        f.write(ret.stdout)
except IOError as e:
    print(f"Error: Failed to write recovered data to '{newfile}': {e}")
    sys.exit(1)

print(f"The contents of the file '{newfile}' are:")
try:
    with open(newfile, 'r') as f:
        print(f.read())
except IOError as e:
    print(f"Error: Failed to read '{newfile}': {e}")