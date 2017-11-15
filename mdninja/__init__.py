# __init__.py

import argparse
from jinja2 import Environment, PackageLoader, FileSystemLoader
import markdown
import sys
import codecs
from pathlib import Path
import os


def render_document(infile, outfile, template):
    """render the document"""
    if not template:
        env = Environment(loader=PackageLoader('mdninja', 'templates'))
        template = env.get_template('default.html')
    else:
        path = Path(outfile).parts
        tfile = path[-1]
        print('tfile: ', tfile)
        print('-1: ', os.path.join(*path[:-1]))
        tdir = os.path.join(*path[:-1])
        if not os.path.isfile(outfile):
            print('template is not a file')
            sys.exit(0)
        env = Environment(loader=FileSystemLoader(tdir))
        template = env.get_template(tfile)
    with open(infile, 'r') as f:
        md = markdown.Markdown(extensions=['markdown.extensions.meta'])
        html = md.convert(f.read())
    content = template.render(body=html, meta=md.Meta)
    if outfile is not None:
        with codecs.open(outfile, 'w', 'utf-8') as fout:
            fout.write(content)
    else:
        sys.stdout.write(content)


def main():
    """Entry point for mdninja"""
    parser = argparse.ArgumentParser('mdninja')
    parser.add_argument('input', help='Input markdown file')
    parser.add_argument('-o', dest='output', help='output file name')
    parser.add_argument('--template', help='template file (Jinja2)')
    args = parser.parse_args()
    render_document(args.input, args.output, args.template)
