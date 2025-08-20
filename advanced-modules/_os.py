import os
from datetime import datetime

# result = dir(os)
# result = os.name

# result = os.chdir(os.path.join(os.path.dirname(__file__), ".."))  # örnek olarak
# result = os.chdir("..\\..\\..")
# result = os.getcwd()

# os.mkdir("new-directory")
# os.makedirs("new-directory/sub-directory")

# os.rename("new-directory", "new-folder")

# os.removedirs("new-directory/sub-directory")

# result = os.listdir()
# result = os.listdir("C:\\")  # bu sistem dizinini listelemeye devam eder

# for file in os.listdir(os.path.join(os.path.dirname(__file__), "advanced-modules")):
#     if file.endswith(".py"):
#         print(file)

# result = os.stat(os.path.join(os.path.dirname(__file__), "advanced-modules", "_datetime.py"))
# result = result.st_size/1024

# result = datetime.fromtimestamp(result.st_birthtime)
# result = datetime.fromtimestamp(result.st_atime)
# result = datetime.fromtimestamp(result.st_mtime)

# os.system("notepad.exe")

base_dir = os.path.dirname(os.path.abspath(__file__))

result = os.path.abspath(os.path.join(base_dir, "advanced-modules", "_datetime.py"))
result = os.path.dirname(os.path.join(base_dir, "advanced-modules", "_datetime.py"))
result = os.path.dirname(os.path.abspath(os.path.join(base_dir, "advanced-modules", "_datetime.py")))
result = os.path.exists(os.path.join(base_dir, "advanced-modules", "_datetime.py"))
result = os.path.exists(os.path.join(base_dir, "advanced-modules"))
result = os.path.isdir(os.path.join(base_dir, "advanced-modules"))
result = os.path.isfile(os.path.join(base_dir, "advanced-modules", "_datetime.py"))
result = os.path.join(base_dir, "try", "try1")
result = os.path.split(os.path.join(base_dir, "advanced-modules", "_os.py"))
result = os.path.splitext(os.path.join(base_dir, "_os.py"))
# result = result[0]
result = result[1]

print(result)
