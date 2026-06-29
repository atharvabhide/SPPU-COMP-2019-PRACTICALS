import os
import re
import subprocess

os.system("clear")

def validate_path(path):
    """Reject shell metacharacters to prevent command injection."""
    if not re.match(r'^[a-zA-Z0-9_./@-]+$', path):
        raise ValueError(f"Invalid input (contains disallowed characters): {path}")
    return path

os.system("echo File Recovery Script")
os.system("echo The list of devices is")
os.system("lsblk")
os.system("echo enter the device to be used")
devname = validate_path(input(""))
imgname = validate_path(input("Enter the image name \n"))
subprocess.run(["dd", "if=" + devname, "of=" + imgname, "bs=512"], check=True)
os.system("echo showing inode number of files")
subprocess.run(["fls", imgname], check=True)
inodeno = validate_path(input("Enter the inode of the deleted file "))
subprocess.run(["istat", imgname, inodeno], check=True)
os.system("echo the contents of the recovered file are")
subprocess.run(["icat", imgname, inodeno], check=True)
os.system("echo enter the name of the file where data to be stored with extension")
newfile = validate_path(input(""))
with open(newfile, "wb") as f:
    subprocess.run(["icat", imgname, inodeno], stdout=f, check=True)
os.system("echo the contents of the file are")
subprocess.run(["cat", newfile], check=True)
