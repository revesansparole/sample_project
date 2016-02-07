import json

p1 = dict(name="read",
          category="oanode",
          module="testio",
          function="read",
          info1="toto was here")

with open("testio.json", 'w') as f:
    json.dump(p1, f, sort_keys=True, indent=4)
