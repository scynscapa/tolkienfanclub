from copystatic import copy_static
from generatepage import generate_page

def main():
    copy_static()
    generate_page("content/index.md", "template.html", "public/index.html")

if __name__ == "__main__":
    main()