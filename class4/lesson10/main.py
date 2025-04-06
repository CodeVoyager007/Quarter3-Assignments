#lesson 10
# 1. Basic File Writing Example
print("1. Basic File Writing Example:")
with open('example.txt', 'w') as file:
    file.write("Hello, World!\n")
    file.write("This is a test file.\n")
    file.writelines(["Line 3\n", "Line 4\n"])
print("File 'example.txt' created and written successfully.")
print()

# 2. Reading File Content
print("2. Reading File Content:")
with open('example.txt', 'r') as file:
    content = file.read()
    print("Full content:")
    print(content)
print()

# 3. Reading Line by Line
print("3. Reading Line by Line:")
with open('example.txt', 'r') as file:
    print("Content line by line:")
    for line in file:
        print(line.strip())
print()

# 4. File Pointer Operations
print("4. File Pointer Operations:")
with open('example.txt', 'r') as file:
    print("Initial position:", file.tell())
    first_line = file.readline()
    print("After reading first line:", file.tell())
    file.seek(0)
    print("After seek(0):", file.tell())
print()

# 5. Appending to File
print("5. Appending to File:")
with open('example.txt', 'a') as file:
    file.write("This is an appended line.\n")
print("Line appended successfully.")
print()

# 6. Exclusive Creation Mode
print("6. Exclusive Creation Mode:")
try:
    with open('new_file.txt', 'x') as file:
        file.write("This is a new file.\n")
    print("New file created successfully.")
except FileExistsError:
    print("File already exists!")
print()

# 7. Binary File Operations
print("7. Binary File Operations:")
with open('binary_file.bin', 'wb') as file:
    file.write(b'This is binary data')
print("Binary file created successfully.")
print()

# 8. File Copy Function
print("8. File Copy Function:")
def copy_file(source, destination):
    try:
        with open(source, 'r') as src, open(destination, 'w') as dest:
            for line in src:
                dest.write(line)
        print(f"File copied from '{source}' to '{destination}' successfully.")
    except FileNotFoundError:
        print(f"Error: File '{source}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

copy_file('example.txt', 'example_copy.txt')
print()

# 9. Reading Specific Lines
print("9. Reading Specific Lines:")
with open('example.txt', 'r') as file:
    lines = file.readlines()
    print("First line:", lines[0].strip())
    print("Last line:", lines[-1].strip())
print()

# 10. File Operations with Error Handling
print("10. File Operations with Error Handling:")
def safe_file_operation(filename, mode='r'):
    try:
        with open(filename, mode) as file:
            if mode == 'r':
                return file.read()
            elif mode == 'w':
                file.write("New content")
                return "File written successfully"
    except FileNotFoundError:
        return f"Error: File '{filename}' not found"
    except PermissionError:
        return f"Error: Permission denied for '{filename}'"
    except Exception as e:
        return f"An error occurred: {e}"

print(safe_file_operation('example.txt'))
print()

# 11. Using r+ Mode (Read and Write)
print("11. Using r+ Mode (Read and Write):")
with open('example.txt', 'r+') as file:
    content = file.read()
    print("Original content:", content)
    file.seek(0)
    file.write("Modified first line\n")
print("File modified successfully.")
print()

# 12. File Size Check
print("12. File Size Check:")
import os
file_size = os.path.getsize('example.txt')
print(f"Size of 'example.txt': {file_size} bytes")
print()

# 13. File Existence Check
print("13. File Existence Check:")
if os.path.exists('example.txt'):
    print("File 'example.txt' exists")
else:
    print("File 'example.txt' does not exist")
print()

# 14. Cleanup (Optional)
print("14. Cleanup:")
try:
    os.remove('example_copy.txt')
    print("Temporary files cleaned up")
except FileNotFoundError:
    print("No temporary files to clean up")
print()
