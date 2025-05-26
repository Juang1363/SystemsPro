import os
import sys
import pwd
import grp
from stat import S_ISBLK, S_ISCHR, S_ISDIR, S_ISDOOR, S_ISGID, S_ISLNK, S_ISREG, S_ISSOCK, S_ISUID, S_ISVTX, S_IXGRP, S_IXOTH, S_IXUSR


def file_type_letter(mode: int) -> str:
    """Return file type letter based on mode."""
    c = '?'
    if S_ISREG(mode):
        c = '-'
    elif S_ISDIR(mode):
        c = 'd'
    elif S_ISBLK(mode):
        c = 'b'
    elif S_ISCHR(mode):
        c = 'c'
    elif S_ISLNK(mode):
        c = 'l'
    elif S_ISSOCK(mode):
        c = 's'
    elif S_ISDOOR(mode):
        c = 'D'
    return c


def ls_perms(mode: int) -> str:
    """Return permission string similar to `ls -l`."""
    rwx = ["---", "--x", "-w-", "-wx", "r--", "r-x", "rw-", "rwx"]
    bits = [0] * 10
    bits[0] = file_type_letter(mode)
    bits[1] = rwx[(mode >> 6) & 7]
    bits[4] = rwx[(mode >> 3) & 7]
    bits[7] = rwx[(mode & 7)]
    if mode & S_ISUID:
        bits[3] = 's' if (mode & S_IXUSR) else 'S'
    if mode & S_ISGID:
        bits[6] = 's' if (mode & S_IXGRP) else 'l'
    if mode & S_ISVTX:
        bits[9] = 't' if (mode & S_IXOTH) else 'T'
    bits = [i for i in bits if i != 0]
    return ''.join(bits)


def show_details(directory, ext=None):
    """Display file details similar to `ls -l`."""
    for root, dirs, files in os.walk(directory):
        for file in files:
            if ext and not file.endswith(ext):
                continue
            filepath = os.path.join(root, file)
            file_stat = os.stat(filepath)
            mode = file_stat.st_mode
            size = file_stat.st_size
            perms = ls_perms(mode)
            owner_name = pwd.getpwuid(file_stat.st_uid).pw_name
            group_name = grp.getgrgid(file_stat.st_gid).gr_name
            print(f"File: {file}")
            print(f"Permissions: {perms}")
            print(f"Owner: {owner_name}")
            print(f"Group: {group_name}")
            print(f"Size: {size} bytes\n")


def search_files(directory, ext, search_keyword):
    """Search for a keyword in files and display details if found."""
    for root, dirs, files in os.walk(directory):
        for file in files:
            if ext and not file.endswith(ext):
                continue
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r') as f:
                    content = f.read()
                    if search_keyword in content:
                        file_stat = os.stat(filepath)
                        mode = file_stat.st_mode
                        perms = ls_perms(mode)
                        owner_name = pwd.getpwuid(file_stat.st_uid).pw_name
                        group_name = grp.getgrgid(file_stat.st_gid).gr_name
                        print(f"Keyword '{search_keyword}' found in {file}")
                        print(f"Permissions: {perms}")
                        print(f"Owner: {owner_name}")
                        print(f"Group: {group_name}\n")
            except (IOError, OSError) as e:
                print(f"Could not read file {filepath}: {e}")


def main():
    if len(sys.argv) < 4:
        print("Usage: python3 yourname_hw3.py <operation> <ext> <directory> [search_keyword]")
        sys.exit(1)

    operation = sys.argv[1]
    ext = sys.argv[2]
    directory = sys.argv[3]

    if operation == "details":
        show_details(directory, ext)
    elif operation == "search" and len(sys.argv) == 5:
        search_keyword = sys.argv[4]
        search_files(directory, ext, search_keyword)
    else:
        print("Invalid operation or missing arguments. Usage: python3 yourname_hw3.py <operation> <ext> <directory> [search_keyword]")
        sys.exit(1)


if __name__ == "__main__":
    main()
