import os

# Custom exception classes
class PermissionError(Exception):
    pass

class InvalidDirectoryError(Exception):
    pass

# Function to handle permission errors
def handle_permission_error():
    raise PermissionError("Error: Permission denied. You don't have sufficient permissions to perform this operation.")

# Function to handle invalid directory errors
def handle_invalid_directory_error():
    raise InvalidDirectoryError("Error: Invalid directory. The specified directory does not exist.")

def create_directory(directory):
    try:
        # Check if the user has permission to create a directory
        if not os.access(directory, os.W_OK):
            handle_permission_error()

        # Check if the directory already exists
        if os.path.exists(directory) and os.path.isdir(directory):
            raise FileExistsError("Error: Directory already exists.")

        # Create the directory
        os.mkdir(directory)
        print("Directory created successfully.")
    except PermissionError as e:
        print(e)
    except FileExistsError as e:
        print(e)
    except Exception as e:
        print("An unexpected error occurred:", e)

def delete_directory(directory):
    try:
        # Check if the user has permission to delete the directory
        if not os.access(directory, os.W_OK):
            handle_permission_error()

        # Check if the directory exists
        if not os.path.exists(directory) or not os.path.isdir(directory):
            handle_invalid_directory_error()

        # Delete the directory
        os.rmdir(directory)
        print("Directory deleted successfully.")
    except PermissionError as e:
        print(e)
    except InvalidDirectoryError as e:
        print(e)
    except Exception as e:
        print("An unexpected error occurred:", e)
