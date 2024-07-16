import pathlib
import re

def get_paths(topdir, pattern):
    for path in pathlib.Path(topdir).rglob(pattern):
        if path.exists():
            yield path

def get_files(paths):
    for path in paths:
        with path.open("rt", encoding="latin-1") as file:
            yield file

def get_lines(files):
    for file in files:
        yield from file 

def get_comments(lines):
    for line in lines:
        m = re.match(r".*(#.*)$", line)
        if m:
            yield m.group(1)

def print_matching(lines, substring):
    for line in lines:
        if substring in line:
            print(line)

paths = get_paths("c:/Users/SP8ky/yokota/pftp/Puzzle1", "*.py")
files = get_files(paths)
lines = get_lines(files)
comments = get_comments(lines)
print_matching(comments, "caps")