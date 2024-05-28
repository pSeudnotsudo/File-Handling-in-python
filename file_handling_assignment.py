# File Creation
try:
    with open("my_file.txt", "w") as file:
        file.write("Hello, This is me Again!\n")
        file.write("This is a Python file handling assignment.\n")
        file.write("The current year is: 2024\n")
except FileNotFoundError:
    print("FileNotFoundError: The file 'my_file.txt' was not found.")
except PermissionError:
    print("PermissionError: You do not have permission to write to 'my_file.txt'.")
finally:
    print("File creation and writing completed.")

# File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        content = file.read()
        print("\nFile content:")
        print(content)
except FileNotFoundError:
    print("FileNotFoundError: The file 'my_file.txt' was not found.")
except PermissionError:
    print("PermissionError: You do not have permission to read 'my_file.txt'.")

# File Appending
try:
    with open("my_file.txt", "a") as file:
        file.write("\nAppended line 1.\n")
        file.write("Appended line 2.\n")
        file.write("Appended line 3.\n")
except FileNotFoundError:
    print("FileNotFoundError: The file 'my_file.txt' was not found.")
except PermissionError:
    print("PermissionError: You do not have permission to append 'my_file.txt'.")
finally:
    print("File appending completed.")

