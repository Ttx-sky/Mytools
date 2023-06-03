import json
from demjson3 import *


def getMy(name=None, r="r", encode="utf-8"):
    with open(name, f'{r}', encoding=encode) as summ:
        summ = summ.read()
    return summ


name = getMy(name=r"js/js.json")
name = json.loads(name)
main = name["main"]
for i in main:  # 总列表
    print(f"阵营:{i}")
    for a in main[i]:  # 阵营
        print(f"角色:{a}")
        z = main[i]
        for b in z[a]:  # 角色
            print(f"技能:{b}")
            try:
                a = z[a]
                for d in a[b]:  # Use， CD
                    q = a[b]
                    for use in q:
                        pass
                    print(f"{use}:{q[use]}")
            except:
                break

