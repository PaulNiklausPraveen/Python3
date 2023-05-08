import os
import shutil

# Local folder you want to copy
source_folder = '/path/to/local/folder'

# Network share information
network_share = '\\\\server\\share'
username = 'your_username'
password = 'your_password'
mount_point = '/mnt/network_share'

# Destination folder on the network share
destination_folder = f'{mount_point}/destination_folder'

# Mount the network share (if not already mounted)
if not os.path.ismount(mount_point):
    os.makedirs(mount_point, exist_ok=True)
    os.system(f'mount -t cifs {network_share} {mount_point} -o username={username},password={password}')

# Copy the folder to the network path
shutil.copytree(source_folder, destination_folder)

# Unmount the network share (optional)
os.system(f'umount {mount_point}')
