import os

def list_directory_contents(path='./New Folder'):
    try:
        # Get the list of all files and directories in the specified path
        entries = os.listdir(path)
        
        print(f"Contents of '{path}':")
        for entry in entries:
            print(entry)
    except FileNotFoundError:
        print(f"The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access '{path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
list_directory_contents('./Python')  # Lists contents of the current directory
