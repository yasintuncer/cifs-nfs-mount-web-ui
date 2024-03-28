from setuptools import setup, find_packages
import os
import subprocess
from scripts.directory import create_directory, delete_directory  # Assuming directory.py is in a folder named 'scripts'
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

mount_point = os.getenv('MOUNT_POINT')

# Update package manager and install cifs-utils
os.system('apt-get update -y')
os.system('apt-get install cifs-utils -y')

# get file path
file_path = os.path.dirname(os.path.abspath(__file__))

## clone uix
os.system(f'cd {file_path}/packages && git clone https://github.com/aitsis/uix.git')
os.system(f'cd {file_path}/packages/uix && pip install -e .')

## clone uix-components
os.system(f'cd {file_path}/packages && git clone https://github.com/aitsis/uix-components.git')
os.system(f'cd {file_path}/packages/uix-components && pip install -e .')

# create mnt directory
try:
    create_directory(mount_point)
except PermissionError as e:
    print(f"Permission denied to create directory {mount_point}: {e}")
    exit(1)
except FileExistsError:
    print(f"Directory {mount_point} already exists.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    exit(1)
