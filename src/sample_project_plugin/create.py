import json

p1 = dict(name="read",
          category="oanode",
          module="testio",
          function="read",
          description="toto was here")

with open("testio.json", 'w') as f:
    json.dump(p1, f, sort_keys=True, indent=4)


p2 = dict(name="workflow",
          category="oaworkflow",
          description="compare binarization algorithms")

with open("workflow.json", 'w') as f:
    json.dump(p2, f, sort_keys=True, indent=4)

