# cat ghtml.py
#!/usr/bin/env python
# coding=utf-8
# code from www.361way.com
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import os
from jinja2 import Environment, FileSystemLoader
PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, 'templates')),
    trim_blocks=False)
def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)
def create_index_html():
    fname = "output.html"

    Groups=[
        {
            "adddate":"1",
            "lastmodified":"null",
            "name":"name",
            "urls":[{"url":"www.baidu.com","date":"1222","description":"baidu"}]
         },
        {
            "adddate":"1",
            "lastmodified":"null",
            "name":"name",
            "urls":[{"url":"www.baidu.com","date":"1222","description":"baidu"}]
        }
    ]
    context = {
        'Groups':  Groups
    }
    with open(fname, 'w') as f:
        html = render_template('bookmarks.html', context)
        f.write(html)
def main():
    create_index_html()
########################################
if __name__ == "__main__":
    main()
