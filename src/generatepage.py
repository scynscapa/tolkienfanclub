import os
from markdowntoblocks import markdown_to_html_node


def extract_title(markdown):
    lines = markdown.split("\n")
    line = lines[0]
    if line[0] != "#" or line[1] != " ":
        raise Exception("title not found in markdown")
    
    return line.lstrip("# ")

def generate_page(from_path, template_path, dest_path):
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
    
    html = html.replace("{{ Title }}", title)
    html = html.replace("{{ Content }}", html)

    if not os.path.exists(os.path.dirname(dest_path)):
        os.makedirs(os.path.dirname(dest_path))

    with open(dest_path, "w") as h:
        h.write(html)
    
