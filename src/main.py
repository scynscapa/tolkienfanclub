from copystatic import copy_static
from generatepage import generate_pages_recursive

def main():
    copy_static()
    #generate_page("content/index.md", "template.html", "public/index.html")
    generate_pages_recursive("content", "template.html", "public")

if __name__ == "__main__":
    main()