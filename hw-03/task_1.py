from pathlib import Path
import argparse
import shutil


# ANSI escape codes for colored output
COLOR_BLUE = "\033[94m"
COLOR_RESET = "\033[0m"


def parse_arguments():
    parser = argparse.ArgumentParser(description="Recursively copy and sort files by extension.")
    parser.add_argument("src_dir", help="Source directory to copy files from")
    parser.add_argument("dest_dir", nargs="?", default="dist", help="Destination directory (default: dist)")
    return parser.parse_args()


def display_tree(path: Path, indent: str = "", prefix: str = "") -> None:
    if path.is_dir():
        # Use blue color for directories
        print(indent + prefix + COLOR_BLUE + str(path.name) + COLOR_RESET)
        indent += "    " if prefix else ""

        # Get a sorted list of children, with directories last
        children = sorted(path.iterdir(), key=lambda x: (x.is_file(), x.name))

        for index, child in enumerate(children):
            # Check if the current child is the last one in the directory
            is_last = index == len(children) - 1
            display_tree(child, indent, "└── " if is_last else "├── ")
    else:
        print(indent + prefix + str(path.name))



def copy_and_sort_files(src: Path, dest: Path):
    for item in src.iterdir():
        if item.is_dir():
            # Recursively call the function for subdirectories
            copy_and_sort_files(item, dest)
        elif item.is_file():
            # Get the file file_format
            file_extension = item.suffix[1:] if item.suffix else "no_file_format"
            new_dir = dest / file_extension
            new_dir.mkdir(parents=True, exist_ok=True)
            try:
                shutil.copy2(item, new_dir / item.name)
                print(f"Copied {item} to {new_dir}")
            except Exception as e:
                print(f"Error copying {item}: {e}")


def main():
    args = parse_arguments()
    src_dir = Path(args.src_dir)
    dest_dir = Path(args.dest_dir)

    # Check if the source directory exists
    if not src_dir.is_dir():
        print(f"Source directory {src_dir} does not exist.")
        return

    # Check if destination directory exists
    dest_dir.mkdir(parents=True, exist_ok=True)

    copy_and_sort_files(src_dir, dest_dir)
    print(f"\n{COLOR_BLUE}Directory structure of {dest_dir}:{COLOR_RESET}")
    display_tree(dest_dir)

if __name__ == "__main__":
    main()
