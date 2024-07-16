import pathlib
import re

for path in pathlib.Path(".").rglob("*.py"):
    if path.exists():
        with path.open("rt", encoding = "latin-1") as file:
            for line in file:
                m = re.match(r".*(#.*)$", line)
                if m:
                    comment = m.group(1)
                    if "spam" in comment:
                        print(comment)