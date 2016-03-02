import json
from nbconvert import HTMLExporter
import nbformat

with open("big_notebook.ipynb", 'r') as f:
    nbjson = f.read()

print "validate", nbformat.validate(json.loads(nbjson))

notebook = nbformat.reads(nbjson, 4)

html_exporter = HTMLExporter()
html_exporter.template_file = 'basic'

(body, resources) = html_exporter.from_notebook_node(notebook)


