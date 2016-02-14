import json

p1 = dict(name="read",
          category="oanode",
          description="toto was here",
          author="revesansparole",
          function="testio:read",
          inputs=[dict(name="in1", interface="IInt",
                       value="0", descr="counter"),
                  dict(name="in2", interface="IStr",
                       value="a", descr="unit")],
          outputs=[dict(name="ret", interface="IInt",
                        descr="important result")])

with open("testio.json", 'w') as f:
    json.dump(p1, f, sort_keys=True, indent=4)


p2 = dict(name="workflow",
          category="oaworkflow",
          description="compare binarization algorithms")

with open("workflow.json", 'w') as f:
    json.dump(p2, f, sort_keys=True, indent=4)

