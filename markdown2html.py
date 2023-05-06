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
        sys.stderr
        .write("Usage: ./markdown2html.py <inputfile> <outputfile>\n")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.isfile(input_file):
        sys.stderr.write(f"Missing {input_file}\n")
        sys.exit(1)

    with open(input_file, 'r') as f:
        md = f.read()

    html = markdown.markdown(md)

    with open(output_file, 'w') as f:
        f.write(html)

    sys.exit(0)
