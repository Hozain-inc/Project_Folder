# setting up a file

from pathlib import Path

workspace = Path("workspace_files")
workspace.mkdir(exist_ok=True)
file_path = workspace / "notes.txt"
file_path

# # Create a file
# f = open(file_path, "w", encoding="utf-8")
# f.write("This is the first line in notes.txt\n")
# f.close()

# # Safe-create using 'x' (uncomment to try once)
# f = open(file_path, "x", encoding="utf-8")
# f.write("This file will only be created if it doesn't exist.\n")
# f.close()

# # Open for writing
# f = open(file_path, "w", encoding= "utf-8")
# f.write("Replaced the old content with this line.\n")
# f.close()

# Write to a file

f = open(file_path, "w", encoding="utf-8")
f.write("Shopping List:\n")
f.write(" - Rice\n")
f.write(" - Beans\n")
f.write(" - Garri\n")
f.close()

# Append to a file

f = open(file_path, "a", encoding="utf-8")
f.write(" - Groundnut oil\n")
f.write(" - Maggi\n")
f.close()


# # Read the whole file
# f = open(file_path, "r", encoding="utf-8")
# content = f.read()
# f.close()
# print(content)

# Read line-by-line
# f = open(file_path, "r", encoding="utf-8")
# print("First line:", f.readline().rstrip())
# print("Second line:", f.readline().rstrip())
# f.close()

# # Read as list of lines
# f = open(file_path, "r", encoding="utf-8")
# lines = f.readlines()
# print("Lines list:", [line.rstrip() for line in lines])

#Iterate over lines
# f = open(file_path, "r", encoding="utf-8")
# for line in f:
#     print("->", line.rstrip())
# f.close()

# Write safely using with statement, it automatically closes the file even if an error happens
# with open(file_path, "w", encoding="utf-8") as f:
#    f.write("My Todo List:\n")
#    f.write(" - Revise Python file handling\n")
#    f.write(" - Practice error handling within a function")
#    f.write(" - Practice JSON & CSV\n")

#Append safely
with open(file_path, "a", encoding="utf-8") as f:
    f.write(" - Build a small project\n")
