import os
import shutil

from md_to_htmlnode import markdown_to_html_node
from md_to_block import extract_title

def copy_from_dir_to_dir(from_dir="static", to_dir="public"):
    if not os.path.exists(from_dir):
        raise Exception(f"Invalid path to {from_dir}")

    if os.path.exists(to_dir):
        shutil.rmtree(to_dir)
    os.mkdir(to_dir)
    

    # COPY
    for item in os.listdir(from_dir):
        item_path_from = os.path.join(from_dir, item)
        item_path_to = os.path.join(to_dir, item)
        if os.path.isfile(item_path_from):
            shutil.copy(item_path_from, item_path_to)
            print(f"Copied file: {item_path_from} to {item_path_to}")
        else:
            os.mkdir(item_path_to)
            copy_from_dir_to_dir(item_path_from, item_path_to)

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, encoding="utf-8") as f:
        markdown_content = f.read()
    with open(template_path, encoding="utf-8") as f:
        template_content = f.read()

    html_content = markdown_to_html_node(markdown_content).to_html()
    title = extract_title(markdown_content)
    updated_template = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_content)

    dest_dir = os.path.dirname(dest_path)
    if dest_dir and not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    with open(dest_path, 'w', encoding="utf-8") as f:
        f.write(updated_template)

def generate_page_recursive(dir_path_content, template_path, dest_dir_path, basepath="/"):
    print(f"Generating page from {dir_path_content} to {dest_dir_path} using {template_path}")

    for item in os.listdir(dir_path_content):
        item_path_from = os.path.join(dir_path_content, item)
        item_path_to = os.path.join(dest_dir_path, item)
        if os.path.isfile(item_path_from):
            with open(item_path_from, encoding="utf-8") as f:
                markdown_content = f.read()
            with open(template_path, encoding="utf-8") as f:
                template_content = f.read()
            
            html_content = markdown_to_html_node(markdown_content).to_html()
            title = extract_title(markdown_content)
            updated_template = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_content)
            updated_template = updated_template.replace('href="/', f'href="{basepath}')
            updated_template = updated_template.replace('src="/', f'src="{basepath}')
            
            if dest_dir_path and not os.path.exists(dest_dir_path):
                os.makedirs(dest_dir_path)
            
            with open(item_path_to.replace(".md", ".html"), 'w', encoding="utf-8") as f:
                f.write(updated_template)
        else:
            os.mkdir(item_path_to)
            generate_page_recursive(item_path_from, template_path, item_path_to, basepath)