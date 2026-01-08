import os
import sys
from copystatic import copy_static
from generatepage import generate_pages_recursive

def main():
    copy_static()

    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"

    generate_pages_recursive("content", "template.html", "docs", basepath)

if __name__ == "__main__":
    main()