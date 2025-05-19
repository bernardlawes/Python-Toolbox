import os
import sys

def print_tree(start_path, prefix=""):
    try:
        items = sorted(os.listdir(start_path))
    except PermissionError:
        print(prefix + "└── [Permission Denied]")
        return

    for i, name in enumerate(items):
        path = os.path.join(start_path, name)
        connector = "└── " if i == len(items) - 1 else "├── "
        print(prefix + connector + name)
        if os.path.isdir(path):
            extension = "    " if i == len(items) - 1 else "│   "
            print_tree(path, prefix + extension)

def main():
    if len(sys.argv) > 1:
        root_dir = sys.argv[1]
    else:
        root_dir = "."  # current directory

    print(f"\nDirectory tree for: {os.path.abspath(root_dir)}\n")
    print_tree(root_dir)

if __name__ == "__main__":
    main()