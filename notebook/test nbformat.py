import json
import nbformat

with open("test_graph.ipynb", 'r') as f:
    nbjson = f.read()

print "validate", nbformat.validate(json.loads(nbjson))

node = nbformat.reads(nbjson, 4)

noded = nbformat.from_dict(json.loads(nbjson))
noded4 = nbformat.convert(noded, 4)



