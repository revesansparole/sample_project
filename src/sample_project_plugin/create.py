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
          description="compare binarization algorithms",
          author="revesansparole",
          nodes=[("read", 100, 10),
                 ("node2", 200, 10),
                 ("node3", 150, 100)],
          connections=[(0, "res", 2, "in1"),
                       (1, "res", 2, "in2")])


with open("workflow.json", 'w') as f:
    json.dump(p2, f, sort_keys=True, indent=4)

