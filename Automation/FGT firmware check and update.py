import subprocess
import re

def check_update(device, username, password):
    # Connect to the Fortigate device using SSH
    ssh = subprocess.Popen(["ssh", f"{username}@{device}", password],
                           stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)

    # Send the command to retrieve the firmware information
    ssh.stdin.write(b"get system status\n")
    result = ssh.stdout.read().decode()

    # Extract the firmware information from the result
    match = re.search("Version: ([\d\.]+)", result)
    if match:
        current_firmware = match.group(1)
    else:
        print(f"{device}: Unable to retrieve current firmware information")
        return

    # The latest firmware information cannot be retrieved from the device,
    # so you will need to obtain it from an external source, such as the
    # Fortinet support website. For this example, I will assume that the
    # latest firmware is hardcoded in the code.
    latest_firmware = "7.2.4"

    # Compare the current firmware with the latest firmware
    if current_firmware < latest_firmware:
        # Update the firmware if there is a new version available
        update_firmware(ssh)
    else:
        # Log the result if the firmware is up-to-date
        print(f"{device}: {current_firmware} (Up-to-date)")

def update_firmware(ssh):
    # Send the command to update the firmware
    ssh.stdin.write(b"config system federated-upgrade\n")
    ssh.stdin.write(b"execute upgrade\n")
    result = ssh.stdout.read().decode()

    # Log the result of the firmware update
    print(f"{device}: {current_firmware} (Updated to {latest_firmware})")

# List of Fortigate devices to check and update
devices = ["172.7.7.1"]
username = "adit"
password = "123123"

for device in devices:
    check_update(device, username, password)
