import os
import re
import subprocess

def validate_input(value):
    """Reject shell metacharacters to prevent command injection."""
    if not re.match(r'^[a-zA-Z0-9_./-]+$', value):
        raise ValueError(f"Invalid input (contains disallowed characters): {value}")
    return value

print("Partition Recovery Script")
print("List of devices attached to system is")
os.system("lsblk")
devname = validate_input(input("Enter the device name\n"))

print("Showing partition table")
subprocess.run(["sudo", "fdisk", "-l", "/dev/" + devname], check=True)

pno = validate_input(input("Enter the partition no to recover "))

fdisk_commands = f"n\n\n{pno}\n\n\nw\n"
subprocess.run(
    ["sudo", "fdisk", "/dev/" + devname],
    input=fdisk_commands.encode(),
    check=True
)
