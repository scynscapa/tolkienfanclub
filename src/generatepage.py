import os
from markdowntoblocks import markdown_to_html_node


def extract_title(markdown):
    lines = markdown.split("\n")
    line = lines[0]
    if line[0] != "#" or line[1] != " ":
        raise Exception("title not found in markdown")
    
    return line.lstrip("# ")

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    try:
        with open(from_path, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print("Input file not found")
    except Exception as e:
        print(f"An error occurred: {e}")

    try:
        with open(template_path, "r", encoding="utf-8") as g:
            template = g.read()
    except FileNotFoundError:
        print("Input file not found")
    except Exception as e:
        print(f"An error occurred: {e}")


    title = extract_title(content)
    html = markdown_to_html_node(content).to_html()
    
    result = template.replace("{{ Title }}", title)
    result = result.replace("{{ Content }}", html)

    result = result.replace('href="/', f'href="{basepath}')
    result = result.replace('src="/', f'src="{basepath}')

    if not os.path.exists(os.path.dirname(dest_path)):
        os.makedirs(os.path.dirname(dest_path))

    with open(dest_path, "w") as h:
        h.write(result)
    
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    list_items = os.listdir(dir_path_content)

    for item in list_items:
        full_path = os.path.join(dir_path_content, item)
        dest_path = os.path.join(dest_dir_path, item)

        basename = os.path.basename(dest_path)
        filename = os.path.splitext(basename)[0]
        dest_file = os.path.join(dest_dir_path, filename) + ".html"

        if os.path.isfile(full_path):
            generate_page(full_path, template_path, dest_file, basepath)
        elif os.path.isdir(full_path):
            generate_pages_recursive(full_path, template_path, dest_path, basepath)

