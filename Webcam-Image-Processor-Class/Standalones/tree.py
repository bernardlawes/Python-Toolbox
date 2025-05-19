import os

def print_tree(start_path, prefix=""):
    items = os.listdir(start_path)
    for i, name in enumerate(items):
        path = os.path.join(start_path, name)
        connector = "└── " if i == len(items)-1 else "├── "
        print(prefix + connector + name)
        if os.path.isdir(path):
            extension = "    " if i == len(items)-1 else "│   "
            print_tree(path, prefix + extension)

print_tree(".")