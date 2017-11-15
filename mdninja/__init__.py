# __init__.py

import argparse
from jinja2 import Environment, PackageLoader, FileSystemLoader
import markdown
import sys
import codecs
from pathlib import Path
import os


class MdNinja(object):
    """The main mdninja class"""

    def __init__(self, args):
        self.args = args

    def render_document(self):
        """render the document"""
        if not self.args.template:
            env = Environment(loader=PackageLoader('mdninja', 'templates'))
            template = env.get_template('default.html')
        else:
            path = Path(self.args.outfile).parts
            tfile = path[-1]
            print('tfile: ', tfile)
            print('-1: ', os.path.join(*path[:-1]))
            tdir = os.path.join(*path[:-1])
            if not os.path.isfile(self.args.outfile):
                print('template is not a file')
                sys.exit(0)
            env = Environment(loader=FileSystemLoader(tdir))
            template = env.get_template(tfile)
        with open(self.args.infile, 'r') as f:
            md = markdown.Markdown(extensions=['markdown.extensions.meta'])
            html = md.convert(f.read())
        content = template.render(body=html,
                                  csslocn=self.args.csslocn,
                                  meta=md.Meta)
        if self.args.outfile is not None:
            with codecs.open(self.args.outfile, 'w', 'utf-8') as f:
                f.write(content)
        else:
            sys.stdout.write(content)


def main():
    """Entry point for mdninja"""
    parser = argparse.ArgumentParser('mdninja')
    parser.add_argument('infile',
                        action='store',
                        help='Input markdown file')
    parser.add_argument('-o', dest='outfile', help='output file name')
    parser.add_argument('-c', dest='csslocn', help='location of the CSS file')
    parser.add_argument('--template',
                        dest='template',
                        help='template file (Jinja2)')
    args = parser.parse_args()
    mdn = MdNinja(args)
    mdn.render_document()
