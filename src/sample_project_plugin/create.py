import json
from uuid import uuid1


n1 = dict(id=uuid1().int,
          name="read",
          category="oanode",
          description="read data from resource",
          author="revesansparole",
          function="testio:read",
          inputs=[dict(name="url", interface="IURL",
                       value="", descr="URL of resource to read")],
          outputs=[dict(name="ret", interface="any",
                        descr="red data")])

n2 = dict(id=uuid1().int,
          name="int",
          category="oanode",
          description="Convert number to int",
          author="revesansparole",
          function="testio:int",
          inputs=[dict(name="val", interface="any",
                       value=0, descr="Value to convert")],
          outputs=[dict(name="ret", interface="IInt",
                        descr="input converted to int")])

n3 = dict(id=uuid1().int,
          name="plus",
          category="oanode",
          description="add two numbers",
          author="revesansparole",
          function="testio:plus",
          inputs=[dict(name="in1", interface="IInt",
                       value=0, descr="first value"),
                  dict(name="in2", interface="IInt",
                       value=0, descr="second value")],
          outputs=[dict(name="ret", interface="IInt",
                        descr="result")])

n4 = dict(id=uuid1().int,
          name="print",
          category="oanode",
          description="print value",
          author="revesansparole",
          function="testio:print",
          inputs=[dict(name="in", interface="any",
                       value="", descr="anything")],
          outputs=[dict(name="out", interface="any",
                        descr="just passing in out")])


for ndef in (n1, n2, n3, n4):
    with open("ndef_%s.json" % ndef["name"], 'w') as f:
        json.dump(ndef, f, sort_keys=True, indent=4)

wkf = dict(id=uuid1().int,
           name="workflow",
           category="oaworkflow",
           description="compare binarization algorithms",
           author="revesansparole",
           nodes=[(n1['id'], None, 100, 10),
                  (n2['id'], "node2", 200, 10),
                  (n3['id'], None, 150, 100),
                  (n4['id'], None, 150, 200)],
           connections=[(0, "ret", 2, "in1"),
                        (1, "ret", 2, "in2"),
                        (2, "ret", 3, "in")])


with open("workflow.json", 'w') as f:
    json.dump(wkf, f, sort_keys=True, indent=4)

