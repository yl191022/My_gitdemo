import re

p = re.compile(r"(.*),电话号码(\d+)")
text = """ 
张三,电话号码111111
李四,电话号码222221
王五,电话号码333331
"""

msg = p.findall(text)
print(msg)
