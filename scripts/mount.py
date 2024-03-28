import subprocess

class SupportedFileSystems:
    CIFS = 'cifs'
    NFS = 'nfs'


class Mount:
    def __init__(self, mount_point, remote_path, share_name, file_system, username, password, domain=None):
        self.mount_point = mount_point
        self.remote_path = remote_path
        self.file_system = file_system
        self.username = username
        self.password = password
        self.options = []    
    def add_options(self, options:str):
    
        self.options.append(options)
     def listshareable(self):
        folders = []
        if self.file_system == SupportedFileSystems.CIFS:
            cmd = f'smbclient -L {self.remote_path} -U {self.username}%{self.password}'
            try:
                output = subprocess.check_output(cmd, shell=True)
                output_str = output.decode()
                # Parse output to extract folders
                # Example: Parse 'Disk|Name' line to get folder names
                for line in output_str.splitlines():
                    if '|' in line and 'Disk' not in line:
                        folders.append(line.split('|')[-1].strip())
            except subprocess.CalledProcessError as e:
                raise RuntimeError(f"Error: {e}")
        elif self.file_system == SupportedFileSystems.NFS:
            cmd = f'showmount -e {self.remote_path}'
            try:
                output = subprocess.check_output(cmd, shell=True)
                output_str = output.decode()
                # Parse output to extract folders
                # Example: Parse 'Export list for ...' line to get folder names
                for line in output_str.splitlines():
                    if 'Export list for' not in line:
                        folders.append(line.split()[-1])
            except subprocess.CalledProcessError as e:
                raise RuntimeError(f"Error: {e}")
        else:
            raise ValueError("Unsupported file system.")
        return folders
    
        
