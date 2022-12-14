"""print("\n\n\033[0;37;41m \033[0m Red label for error messages\n")
print("\033[0;37;43m \033[0m Yellow/Orange label for information messages (no action required)\n")
print("\033[0;37;44m \033[0m Blue label for prompts (action required)\n")
print("\033[0;37;45m \033[0m Purple label for new words found while computing\n")
print("\033[0;37;46m \033[0m Teal/Aqua label for output messages; results, progress updates and thank-you message\n")"""

# importing os module
import os

# Directory
directory = "GeeksforGeeks"

# Parent Directory path
parent_dir = "D:/Pycharm projects/"

# Path
path = os.path.join(parent_dir, directory)

# Create the directory
# 'GeeksForGeeks' in
# '/home / User / Documents'
os.mkdir(path)
print("Directory '% s' created" % directory)

# Directory
directory = "Geeks"

# Parent Directory path
parent_dir = "D:/Pycharm projects"

# mode
mode = 0o666

# Path
path = os.path.join(parent_dir, directory)

# Create the directory
# 'GeeksForGeeks' in
# '/home / User / Documents'
# with mode 0o666
os.mkdir(path, mode)
print("Directory '% s' created" % directory)