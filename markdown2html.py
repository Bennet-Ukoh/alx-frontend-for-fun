#!/usr/bin/python3
"""
This script converts a Markdown file to an HTML file
Usage: ./markdown2html.py <inputfile> <outputfile>
"""

import markdown
import sys
import os.path

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)

    README.md = sys.argv[1]
    README.html = sys.argv[2]

    if not os.path.isfile(README.md):
        sys.stderr.write(f"Missing {README.md}\n")
        sys.exit(1)

    with open(README.md, 'r') as f:
        md = f.read()

    html = markdown.markdown(md)

    with open(README.html, 'w') as f:
        f.write(html)

    sys.exit(0)
