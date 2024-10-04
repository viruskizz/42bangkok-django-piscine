import sys
import os
import re

def read_file_content(filename: str, isLines: bool = False):
    try:
        f = open(filename, "r")
        if isLines:
            content = f.readlines()
        else:
            content = f.read()
        f.close()
        return content
    except OSError as e:
        print("Could not open/read file:", filename, file=sys.stderr)
        sys.exit(1)

def read_var_file(filename: str):
    lines = read_file_content(filename, True)
    obj = {}
    for content in lines:
        var = list(map(lambda x:x.strip(" \"\'"), content.strip("\n").split("=")))
        obj[var[0]] = var[1]
    return obj

def create_file(filename, content):
    f = open(filename, "w")
    f.write(content)
    f.close()

def validate_template_file(filename: str):
    if not re.match(r'^.*\.(template)$', filename):
        print("template file extension does not match", file=sys.stderr)
        sys.exit(1)

def create_html_content(template: str, setting: dict):
    try:
        return template.format(**settings)
    except KeyError as e:
        print('KeyError:', e, file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Need only single argument", file=sys.stderr)
        sys.exit(1)
    filename = sys.argv[1]
    validate_template_file(filename)
    template = read_file_content(filename)
    settings = read_var_file("settings.py")
    print(settings)
    if "name" not in settings:
        print("Need name as key in settings.py")
        sys.exit(1)
    content = create_html_content(template, settings)
    htmlfile = "".join(filename.split(".")[:-1]) + '.html'
    create_file(htmlfile, content)
